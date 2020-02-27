from django.urls import path

from .views import DirectoryView, UnitView

app_name = "directories"

urlpatterns = [
    path('directories/', DirectoryView.as_view()),
    path('units/', UnitView.as_view()),
]