# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # включаем URLы из main/urls.py
    path('', include('main.urls')),
]
