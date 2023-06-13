from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

# view for registeration of new members
def registerPage(request):
    form = CreateUserForm()

    # checking form method and saving user if valid
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('user_name')
            messages.success(request, user + ' '+ 'Congratulation!')
            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'users/register.html', context)


# view for login of members
def loginPage(request):

    # checking form method
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, user_name=user_name, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('userpage')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)


# view to logout member
def logoutMember(request):
    logout(request)
    return redirect('landingpage')