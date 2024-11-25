from django.shortcuts import render, redirect 
from .forms import ContactForm
# Create your views here.

def home_view(request):
    return render(request,'introform/home.html')


def contact_view(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
            form = ContactForm()
    context = {'form':form}
    return render(request,'introform/contact.html',context)
    
def contact_success_view(request):
    return render(request, 'introform/contact_success.html')