from django.contrib import admin
from django.urls import path
from MainSite import views
urlpatterns = [
    path('index',views.index, name='Indexpage'),
    path('about',views.about, name='aboutpage')
]