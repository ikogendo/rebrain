from django.shortcuts import render
from django.http import HttpResponse
from .models  import bank
import os
#import settings

#file_path = os.path.join(settings.STATIC_ROOT, 'styles/styles.css')
#with open(file_path,'r') as f:
#      file_style = f.read()
      
# Create your views here.

def  index(request):
    banks= bank.objects.all()
    content = {'banks': banks } #, 'static': file_style }
    return render(request,'home.html',content)
#    return HttpResponse("<center>Welcome to hell</center>")


def secretpage(request):
    return HttpResponse('You found secret page')

def exit(request):
    return render(request,'end.html')