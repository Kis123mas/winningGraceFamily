from django.shortcuts import render, redirect

# Create your views here.

# view for admin dashboard
def adminPage(request):

    context = {}
    return render(request, 'admindash/index.html', context)