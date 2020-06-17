from django.urls import path
from apitest import views

urlpatterns = [
    path('apitest_manage/', views.apitest_manage),
    path('apistep_manage/', views.apistep_manage),
    path('apis_manage/', views.apis_manage),
]
