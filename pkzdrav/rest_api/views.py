from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from .models import Directory, Unit
from .serializer import DirectodySerializer

def pagination(request, object_list, objects_per_page=10):
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
    def get(self, request):
        "Ответ на GET запрос для получения списка справочников"
        try:
            #Проверяем, введена ли дата и введена ли корректно
            date = request.GET.get('date')
            formated_date = datetime.datetime.strptime(date, '%Y%m%d') #Форматирование даты из строки в стандартный вид
            directories_list = Directory.objects.filter(start_date__gt=formated_date)
        except:
            #При неправильно введенной дате возвращает весь список
            directories_list = Directory.objects.all()

        directories = pagination(request, directories_list) #разбивка данных на страницы через paginator
        serializer = DirectodySerializer(directories, many=True)  #сериалайзер необходим для форматирования результата
        return Response({"directories": serializer.data})
