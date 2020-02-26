from rest_framework import serializers

class DirectodySerializer(serializers.Serializer):
    directory_id = serializers.IntegerField()
    name = serializers.CharField(max_length=250)
    short_name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    version = serializers.CharField(max_length=250)
    start_date = serializers.DateField()