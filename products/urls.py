from django.urls import path
from . import views

# ''(root of the app "products")  -->  /products
# 'trending'  --> /products/trending
# 'mens/small' --> /products/mens/small

urlpatterns = [
    path('', views.index),
    path('trending', views.trending)
]
