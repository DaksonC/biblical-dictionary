from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from words.api import viewsets

router = routers.DefaultRouter()

router.register(r'api/v1/words', viewsets.WordViewSet, basename='Words')
router.register(r'admin/login', viewsets.WordViewSet, basename='Login')

urlpatterns = [
    path('api/v1/', include('words.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]
