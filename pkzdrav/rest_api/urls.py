from django.urls import path

from .views import DirectoryView

app_name = "directories"

urlpatterns = [
    path('directories/', DirectoryView.as_view()),
]