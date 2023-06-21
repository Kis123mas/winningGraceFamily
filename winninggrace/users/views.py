from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from landing import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from userdash.models import Member
from userdash.decorators import *



# Create your views here.

# view for registeration of new members
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    # checking form method and saving user if valid
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('user_name')

            group = Group.objects.get(name='member')
            user.groups.add(group)
            Member.objects.create(
                user=user,
            )

            messages.success(request, 'Congratulation!' + username )
            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'users/register.html', context)


# view for login of members
@unauthenticated_user
def loginPage(request):
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