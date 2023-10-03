from django.urls import path
from .api.viewsets import WordViewSet

urlpatterns = [
    path('words/', WordViewSet.as_view({'get': 'list'})),
    path('words/search/', WordViewSet.as_view({'get': 'search'})),
]
