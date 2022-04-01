"""Defines schemas the URL for learning_logs"""

from django.urls import path
from . import  views

app_name = 'learning_logs'
urlpatterns = [
    #home page
#    path('', views.index, name='index'),
    #page with the list all themes
    path('toys/', views.toys, name='toys'),
    ]

