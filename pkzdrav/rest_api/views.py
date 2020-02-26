from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Directory, Unit
from .serializer import DirectodySerializer

class DirectoryView(APIView):
    def get(selfself, request):
        "Ответ на GET запрос для получения списка справочников"
        directories = Directory.objects.all()
        serializer = DirectodySerializer(directories, many=True)
        return Response({"directories": serializer.data})
