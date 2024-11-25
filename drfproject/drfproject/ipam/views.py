from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import station, Build
from .serializers import stationSerializer
# Create your views here.

def index1(request):
    return HttpResponse('dasdasd')

def index2(request):
    return HttpResponse('Hello 2')

def index3(request):
    return HttpResponse('Hello 3')

class stationAPIView(generics.ListAPIView):
    queryset = station.objects.all()
    serializer_class = stationSerializer
    