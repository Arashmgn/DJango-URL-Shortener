from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',url_shortner,name='home'),
    path('<slug:slug>/',url_redirect,name='redirect'),
]
