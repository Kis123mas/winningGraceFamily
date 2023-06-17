from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *

# Create your views here.

# view for admin dashboard
def adminPage(request):

    programs = Program.objects.all()
    events = Event.objects.all()
    recommendedbible = Recommendedbible.objects.all()
    seedofwins = Seedofwin.objects.all()
    announcement = Announcement.objects.all()


    context = {'programs':programs, 'events':events, 'recommendedbible':recommendedbible, 'seedofwins':seedofwins, 'announcement':announcement}
    return render(request, 'admindash/index.html', context)


# view for program form
def programForm(request):

    form = ProgramForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'CREATED NEW PROGRAM.')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/programform.html', context)


# program update form
def updateProgram(request, pk):

    form = ProgramForm()

    context = {'form':form}
    return render(request, 'admindash/programform.html', context)



# view for event form
def eventForm(request):

    form = EventForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'CREATED NEW EVENT')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/eventform.html', context)

# event update form
def updateEvent(request, pk):

    form = EventForm()

    context = {'form':form}
    return render(request, 'admindash/eventform.html', context)



# view for announcement form
def announcementForm(request):

    form = AnnouncementForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'CREATED NEW ANNOUNCEMENT')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/announcementform.html', context)


# announcement update form
def updateAnnouncement(request, pk):

    form = AnnouncementForm()

    context = {'form':form}
    return render(request, 'admindash/announcementform.html', context)



# view for seed of wining grace form   
def seedofwinForm(request):

    form = SeedofwinForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'CREATED NEW SEED OF WINNING GRACE')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/seedofwin.html', context)


# seedofwin update form
def updateSeedofwin(request, pk):

    form = SeedofwinForm()

    context = {'form':form}
    return render(request, 'admindash/seedofwin.html', context)



# view for recommended bible
def recommendedbibleForm(request):

    form = BiblerecommendationForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            messages.success(request, 'CREATED NEW RECOMMENDED BIBLE PASSAGE.')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/recommendedbible.html', context)


# recommended bible update form
def updateRecommendedBible(request, pk):

    form = BiblerecommendationForm()

    context = {'form':form}
    return render(request, 'admindash/recommendedbible.html', context)