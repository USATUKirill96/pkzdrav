from django.db import models

# Create your models here.
class Directory(models.Model):
    """Модель справочника"""
    id = models.AutoField()
    name = models.CharField(max_length=250, verbose_name='Наименование')
    short_name = models.CharField(max_length=250, verbose_name='Короткое наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    version = models.CharField(blank=False, verbose_name='Версия')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата начала действия версии')

    class Meta:
        verbose_name_plural = 'Справочники'
        verbose_name = 'Справочник'
        ordering = ['short_name']


class Directory_unit(models.Model):
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, verbose_name = 'родительский идентификатор')
    id = models.AutoField()
    code = models.CharField(blank=False, verbose_name='Код элемента')
    value = models.CharField(blank=False, verbose_name='Значение элемента')

    class Meta:
        verbose_name_plural = 'Элементы справочника'
        verbose_name = 'Элемент справочника'
        ordering = ['code']