from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

# view for landingpage
def landingPage(request):

    form = ContactForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('landingpage')
            
    context = {'form':form}
    return render(request, 'landing/landing.html', context) 
