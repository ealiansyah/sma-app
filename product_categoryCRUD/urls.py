from django.urls import path

from product_categoryCRUD import views

app_name = 'Product_CategoryCRUD'

urlpatterns = [
    path('', views.category, name='categories'),
    path('details/<str:product_category>', views.details, name='details'),
    path('details/<str:product_category>/update', views.update_desc, name='update')
]