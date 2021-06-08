from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import TodoViewSet

router = routers.DefaultRouter()
router.register(r'task', TodoViewSet, basename='task')

app_name = 'todo'

urlpatterns = [
    path('api/', include(router.urls)),
]