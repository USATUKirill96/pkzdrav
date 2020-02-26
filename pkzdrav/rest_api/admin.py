from django.contrib import admin
from .models import Directory, Unit

# Регистрация сущностей БД в панели администратора
@admin.register(Directory)
class Directory_admin(admin.ModelAdmin):
    list_display = ('directory_id', 'name','short_name', 'version', 'start_date') #Атрибуты, отображаемые в списке всех объектов
    list_display_links = ('directory_id', 'name') #поля-ссылки
    search_fields = ('name', 'version', 'start_date') #поля поиска

@admin.register(Unit)
class Unit_admin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'code', 'value') #атрибуты в списке объектов
    list_display_links = ('id', 'code') #поля-ссылки
    search_fields = ('id',) #поля, по которым будет осуществляться поиск
    raw_id_fields = ("directory",) #Добавляет возможность выбрать родительский справочник, пользуясь поиском
    list_filter = ('directory', )  #фильтрация значений по принадлежности к директории

