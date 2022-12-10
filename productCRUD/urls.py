from django.urls import path

from productCRUD import views

app_name = 'ProductCRUD'

urlpatterns = [
    path('', views.get_product, name='Get Product'),
    path('create/', views.create_product, name='Create Product'),
    path('update/', views.update_product, name='Update Product'),
    path('delete/', views.delete_product, name='Delete Product'),
]