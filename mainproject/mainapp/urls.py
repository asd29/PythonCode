from django.contrib import admin
from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('list', views.list, name='ListPage'),
    ]