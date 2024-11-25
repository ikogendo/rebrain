from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import views
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.

def registry_view(request):
    if request.method =="POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            form = RegisterForm()
            return render(request,'acc/register.html',{'form':form})

def login_view(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'home'
                return redirect(next_url)
            else:
                error_message ="Incorrect user/password"
    return render(request,'acc/login.html', {'errror': error_message})

def logout_view(request):
    pass

@login_required
def home_view(request):
    pass