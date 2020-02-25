from django.contrib import admin
from .models import Directory, Unit

# Регистрация сущностей БД в панели администратора
@admin.register(Directory)
class Directory_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version', 'start_date') #Атрибуты, отображаемые в списке всех объектов
    list_display_links = ('id', 'name') #кликабельные атрибуты
    search_fields = ('name', 'version', 'start_date') #поля поиска

@admin.register(Unit)
class Unit_admin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'code', 'value')
    list_display_links = ('id', 'code')
    search_fields = ('parent_id',)
    raw_id_fields = ("directory",) #Добавляет возможность выбрать родительский справочник, пользуясь поиском
    list_filter = ('directory', )

