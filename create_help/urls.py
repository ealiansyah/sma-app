from django.urls import path
from .views import create_help, delete_help

urlpatterns = [
    path('create/', create_help, name='create_help'),
    path('delete/', delete_help, name='delete_help'),
]