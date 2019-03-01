from django.contrib import admin
from django.urls import path
from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('list', views.list, name='ListPage'),
    path('clientdetails/<int:client_id>', views.client_details , name='ClientDetails'),
    path('updatedetails/<int:client_id>',views.update,name='updatedetails')
    ]