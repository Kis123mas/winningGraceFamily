from django.shortcuts import render, redirect


# Create your views here.


# view for uer dashboard
def userdashPage(request):

    context = {}
    return render(request, 'userdash/index.html', context)


