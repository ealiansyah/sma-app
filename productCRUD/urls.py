from django.urls import path

from productCRUD import views

app_name = 'ProductCRUD'

urlpatterns = [
    path('create/', views.create_product, name='create'),
]