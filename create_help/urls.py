from django.urls import path

urlpatterns = [
    path('create/', views.create_help, name='create_help'),
    path('delete/', views.delete_help, name='delete_help'),
]