from rest_framework import viewsets
from rest_framework import filters

from words.api import serializers
from words import models


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WordSerializer
    queryset = models.Word.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=word']
