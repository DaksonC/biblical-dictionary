from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

from words.api import serializers
from words import models


class CustomPagination(PageNumberPagination):
    page_size = 10  # Defina o número de itens por página aqui
    page_size_query_param = 'page_size'
    max_page_size = 100  # Defina o número máximo de itens por página aqui


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WordSerializer
    queryset = models.Word.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['=word']

    pagination_class = CustomPagination

    def list(self, request):
        search_query = request.query_params.get('search')
        if search_query:
            words = self.queryset.filter(word=search_query)
            if not words.exists():
                raise NotFound('Word not found!')
        else:
            words = self.get_queryset()

        page = self.paginate_queryset(words)
        if page is not None:
            serializer = serializers.WordSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.WordSerializer(words, many=True)

        return Response(serializer.data)
