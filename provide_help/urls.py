from django.urls import path
from .views import get_help_list, provide_help

urlpatterns = [
    path('', get_help_list, name='provide_help'),
    path('view_ticket/', provide_help, name='list_help'),
]