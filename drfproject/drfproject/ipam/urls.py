from django.urls  import path
from django.shortcuts import render
from . import views

urlpatterns = [
#    path('', views.index1 ),
    path('ipam/', views.index1 ),
    path('ipam/2', views.index2 ),
    path('ipam/3', views.index3 ),
    path('api/v1/list/',views.stationAPIView.as_view() )
#    path('esd/', admin.site.urls)
]