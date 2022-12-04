from django.urls import path

from checkout import views

app_name = 'Checkout'

urlpatterns = [
  path('search/', views.search_products, name='Search Products'),
  path('checkout/', views.post_checkout, name='Post Checkout'),
]