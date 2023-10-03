from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from words.api import serializers
from words import models


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WordSerializer
    queryset = models.Word.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=word']

    def list(self, request):
        search_query = request.query_params.get('search')
        if search_query:
            words = self.queryset.filter(word=search_query)
            if not words.exists():
                raise NotFound('Word not found!')
        else:
            words = self.get_queryset()

        serializer = serializers.WordSerializer(words, many=True)

        return Response(serializer.data)
