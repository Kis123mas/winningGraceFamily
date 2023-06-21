from django.shortcuts import render, redirect
from .forms import MemberForm, PrayerForm
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from users.urls import *
from django.contrib.auth.models import User
from userdash.decorators import *

# Create your views here.


# view for uer dashboard
@login_required(login_url='loginpage')
def userdashPage(request):
    programs = Program.objects.all()
    events = Event.objects.all()
    recommendedbible = Recommendedbible.objects.all()
    seedofwins = Seedofwin.objects.all()
    announcement = Announcement.objects.all()


    context = {'programs':programs, 'events':events, 'recommendedbible':recommendedbible, 'seedofwins':seedofwins, 'announcement':announcement}
    return render(request, 'userdash/index.html', context)




# view for userprofile
@login_required(login_url='login')
@allowed_users(allowed_roles=['member', 'admin'])
def profilePage(request):

    member = request.user.member
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'userdash/users-profile.html', context)


# view for prayer request
@login_required(login_url='login')
@allowed_users(allowed_roles=['member'])
def prayerRequestPage(request):

    form = PrayerForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'Congratulations! Your Prayer Request Have Been Submitted.')
            return redirect('userpage')

    context = {'form':form}
    return render(request, 'userdash/prayerrequest.html', context)