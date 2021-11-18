from rest_framework import serializers



class Nameseraializer(serializers.Serializer):
    name = serializers.CharField(max_length=7)