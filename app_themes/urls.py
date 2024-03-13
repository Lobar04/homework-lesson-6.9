from django.urls import path

from .views import theme_table,main

urlpatterns = [
    path('themes/',theme_table,name = 'theme_url'),
    path('',main, name = 'main_url')
]