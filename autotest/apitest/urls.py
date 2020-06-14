from django.contrib import admin
from django.urls import path, include
from apitest import views

urlpatterns = [
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage),

]
