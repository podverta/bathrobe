"""Defines schemas the URL for learning_logs"""

from django.urls import path
from . import views

app_name = 'bb'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #page with the list all themes
    path('toys/', views.toys, name='toys'),
    path('towels/', views.towels, name='towels'),
    path('bathrobes/', views.bathrobes, name='bathrobes'),
    path('edit_towels/<int:towels_id>/', views.edit_towels, name='edit_towels'),
    ]

