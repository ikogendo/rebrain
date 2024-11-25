from django.urls  import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.index ),
    path('sp',views.secretpage),
    path('exit',views.exit),
]
