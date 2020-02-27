from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.http import Http404

from .models import Directory, Unit
from .serializer import DirectodySerializer, UnitSerializer

def pagination(request, object_list, objects_per_page=5):
    """Функция разбивки объекты на страницы. Принимает реквест для определения
    номера страницы, список объектов и число объектов на страницу (стандартно 10)"""
    paginator = Paginator(object_list, objects_per_page)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)  # Попытаться отобразить нужную страницу (после разбивки через paginator)
    except PageNotAnInteger:
        objects = paginator.page(1)  # Если пользователь запросил не целый номер, вернуть первую
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)  # Если номер страницы больше существующего, вернуть последнюю
    return objects


class DirectoryView(APIView):
    """Класс для работы со справочниками"""
    def get(self, request):
        "Ответ на GET запрос для получения списка справочников"
        try:
            #Проверяем, введена ли дата и введена ли корректно
            date = request.GET.get('date')
            formated_date = datetime.datetime.strptime(date, '%Y%m%d') #Форматирование даты из строки в стандартный вид
            directories_list = Directory.objects.filter(start_date__gt=formated_date)
        except:
            if date == 'all':
                directories_list = Directory.objects.all()
            else:
                #При неправильно введенной дате возвращает 404
                raise Http404

        directories = pagination(request, directories_list) #разбивка данных на страницы через paginator
        serializer = DirectodySerializer(directories, many=True)  #сериалайзер необходим для форматирования результата
        return Response({"directories": serializer.data})

class UnitView(APIView):
    """Класс для работы с элементами справочника"""
    def get_atributes(self, request):
        """Получает из запроса данные для фильтрации элементов. При некорректно введенном запросе или отсутствии
        элементов возвращает 404"""
        try:
            id = request.GET.get('id')
            version = request.GET.get('version')
            action = request.GET.get('action')
        except:
            raise Http404

        return id, version, action

    def validate(self, directory_id, version, request):
        """Валидация элементов справочника"""
        try:
            id = request.GET.get('code')
            value = request.GET.get('value')
        except:
            raise Http404

        tested_elements = self.pull(directory_id, version) #Обращение к функции pull для получения списка элементов
        for unit in tested_elements: #Поиск совпадения кода элемента с его значением
            if unit.code == id and unit.value == value:
                return True
        return False



    def pull(self, id, version):
        """Получение элементов справочника. Сначала отыскивается идентификатор справочника по заданным критериям"""
        if version == 'actual': #Действия при поиске актуального справочника
            actual_version_object = Directory.objects.filter(directory_id=id).order_by('version').last()
            parent_id = actual_version_object.id
        else: #Действия при поиске конкретного справочника
            requested_version_object = Directory.objects.get(version=version, directory_id=id)
            parent_id = requested_version_object.id
        #После нахождения айдти справочника, выбираются его дочерние элементы
        elements_list = Unit.objects.filter(directory__id=parent_id)
        return elements_list




    def get(self, request):
        #Проверяется значение атрибута action для разграничения действий по валидации и получению списка
        id, version, action = self.get_atributes(request)
        if action == 'get':
            answer = self.pull(id=id, version=version)
            elements = pagination(request, answer)
            serializer = UnitSerializer(elements, many=True)
            return Response({"Units": serializer.data})
        elif action == 'validate':
            answer = self.validate(directory_id=id, version=version, request=request)
            return Response({"Validation":answer})
        else:
            raise Http404
