from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.inicio,name='inicio'),
    path('cargar_json/', views.cargar_json, name='cargar_json')
]
