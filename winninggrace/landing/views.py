from django.shortcuts import render, redirect

# Create your views here.

# view for landingpage
def landingPage(request):
    context = {}
    return render(request, 'landing/landing.html', context) 