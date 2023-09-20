from rest_framework import viewsets
from words.api import serializers
from words import models


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WordSerializer
    queryset = models.Words.objects.all()
