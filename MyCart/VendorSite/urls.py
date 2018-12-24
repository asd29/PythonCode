from django.contrib import admin
from django.urls import path
from VendorSite import views
urlpatterns = [
    path('home',views.home, name='Homepage')
    ]