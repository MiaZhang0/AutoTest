from django.urls import path
from product import views

urlpatterns = [
    path('product_manage/', views.product_manage),
]