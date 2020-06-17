from django.urls import path
from bug import views

urlpatterns = [
    path('bug_manage/', views.bug_manage),
]