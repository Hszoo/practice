from django.contrib import admin
from django.urls import path, include
from menus import views

urlpatterns = [
    path('', views.menushome),
]
