from django.contrib import admin
from .models import Directory, Unit

# Регистрация сущностей БД в панели администратора

class Directory_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version', 'start_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'version', 'start_date')

class Unit_admin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'code', 'value')
    list_display_links = ('id', 'code')
    search_fields = ('id', 'parent_id', 'code')


admin.site.register(Directory, Directory_admin)
admin.site.register(Unit, Unit_admin)