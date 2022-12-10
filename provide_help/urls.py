from django.urls import path

urlpatterns = [
    path('create/', views.provide_help, name='provide_help'),
    path('view_list/', views.get_help_list, name='list_help'),
]