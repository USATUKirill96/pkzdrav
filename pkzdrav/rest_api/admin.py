from django.contrib import admin
from .models import Directory, Unit

# Регистрация сущностей БД в панели администратора
@admin.register(Directory)
class Directory_admin(admin.ModelAdmin):
    list_display = ('id', 'directory_id', 'version', 'name', 'short_name', 'start_date') #Атрибуты, отображаемые в списке всех объектов
    list_display_links = ('directory_id', 'name') #поля-ссылки
    search_fields = ('name', 'version', 'start_date') #поля поиска

@admin.register(Unit)
class Unit_admin(admin.ModelAdmin):
    list_display = ('id', 'directory', 'code', 'value') #атрибуты в списке объектов
    list_display_links = ('id', 'code', 'directory') #поля-ссылки
    search_fields = ('code',) #поля, по которым будет осуществляться поиск
    raw_id_fields = ("directory",) #Добавляет возможность выбрать родительский справочник, пользуясь поиском
    list_filter = ('directory', )  #фильтрация значений по принадлежности к директории

