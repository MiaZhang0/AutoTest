from django.urls import path

from apptest import views

urlpatterns = [
    path('appcase_manage/', views.appcase_manage),
    path('appcasestep_manage',views.appcasestep_manage),
]