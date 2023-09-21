from rest_framework import serializers
from words import models


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = '__all__'
        search_fields = ['word']
