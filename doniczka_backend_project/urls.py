from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doniczka_backend_app import views

router = DefaultRouter()

router.register(r'plants', views.PlantViewSet, 'plants')

urlpatterns = [
    path('', include(router.urls))
]
