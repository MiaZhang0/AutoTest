from django.urls import path
from set import views

urlpatterns = [
    path('set_manage/', views.set_manage),
    path('set_user/',views.set_user),
]
