from django.urls import path
from webtest import views

urlpatterns = [
    path('webcase_manage/',views.webcase_manage),
    path('webcasestep_manage/',views.webcasestep_manage)
]