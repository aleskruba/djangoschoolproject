from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('addstudent', views.registerPage, name='addstudent')
]
