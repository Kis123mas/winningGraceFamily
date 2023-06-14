from django.shortcuts import render, redirect
from .forms import MemberForm


# Create your views here.


# view for uer dashboard
def userdashPage(request):

    context = {}
    return render(request, 'userdash/index.html', context)


# view for userprofile
def profilePage(request):

    member = request.user.member
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'userdash/users-profile.html', context)
