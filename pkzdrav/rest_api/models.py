from django.db import models

# Create your models here.
class Directory(models.Model):
    """Модель справочника"""
    id = models.AutoField(primary_key=True)
    directory_id = models.IntegerField(default=0, verbose_name='Идентификатор справочника')
    name = models.CharField(max_length=250, verbose_name='Наименование')
    short_name = models.CharField(max_length=250, verbose_name='Короткое наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    version = models.CharField(max_length=250, blank=False, verbose_name='Версия')
    start_date = models.DateField(verbose_name='Дата начала действия версии')

    class Meta:
        """Преобразует вывод в панели администратора в удобочитаемый"""
        verbose_name_plural = 'Справочники'
        verbose_name = 'Справочник'
        unique_together = ('directory_id', 'version')  #Определяет уникальную совокупность полей

    def __str__(self):
        return f"Справочник {self.name}, идентификатор {self.directory_id}, версия {self.version}"



class Unit(models.Model):
    """Модель элемента справочника"""
    id = models.AutoField(primary_key=True) #идентификатор элемента
    directory = models.ForeignKey(Directory, on_delete=models.CASCADE, verbose_name = 'родительский справочник')
    parent_id = Directory.id #родительский идентификатор
    code = models.CharField(max_length=250, blank=False, verbose_name='Код элемента')
    value = models.CharField(max_length=250, blank=False, verbose_name='Значение элемента')

    class Meta:
        "Преобразует вывод в панели администратора"
        verbose_name_plural = 'Элементы справочника'
        verbose_name = 'Элемент справочника'
        ordering = ['code']

    def __str__(self):
        return f"{self.directory}, {self.code}"