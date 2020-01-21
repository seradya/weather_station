# -*- coding: utf-8 -*-
from django.urls import path
from main import views


urlpatterns = [
    path('', views.main, name='main')
]
