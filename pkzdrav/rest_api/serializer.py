from rest_framework import serializers

"""Предназначен для форматирования данных из базы в формат REST API. Объявленные классы соответствуют моделям, поля 
аналогичны. Поле TextField заменяется на CharField без указания максимальной длины. Названия атрибутов
соответствуют таковым у преобразуемой модели."""

class DirectodySerializer(serializers.Serializer):
    directory_id = serializers.IntegerField()
    name = serializers.CharField(max_length=250)
    short_name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    version = serializers.CharField(max_length=250)
    start_date = serializers.DateField()

class UnitSerializer(serializers.Serializer):
    id = serializers.CharField()  # идентификатор элемента
    parent_id = serializers.CharField()  # родительский идентификатор
    code = serializers.CharField(max_length=250)
    value = serializers.CharField(max_length=250)