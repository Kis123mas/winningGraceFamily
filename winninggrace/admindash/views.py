from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from users.urls import *
from userdash.decorators import *

# Create your views here.

# view for admin dashboard

@login_required(login_url='loginpage')
@admin_only
def adminPage(request):

    programs = Program.objects.all()
    events = Event.objects.all()
    recommendedbible = Recommendedbible.objects.all()
    seedofwins = Seedofwin.objects.all()
    announcement = Announcement.objects.all()


    context = {'programs':programs, 'events':events, 'recommendedbible':recommendedbible, 'seedofwins':seedofwins, 'announcement':announcement}
    return render(request, 'admindash/index.html', context)


#+-------------ALL VIEWS FOR PROGRAM --------------+

# view for program form
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateProgram(request, pk):

    program = Program.objects.get(id=pk)
    form = ProgramForm(instance=program)

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid:
            form.save()
            messages.success(request, 'PROGRAM UPDATED.')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/programform.html', context)

# view to delete program
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteProgram(request, pk):
    program = Program.objects.get(id=pk)

    if request.method == 'POST':
        program.delete()
        messages.success(request, 'DELETED')
        return redirect('adminpage')
    context = {'item':program}
    return render(request, 'admindash/delete.html', context)


#+-------------ALL VIEWS FOR EVENT --------------+
# view for event form
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateEvent(request, pk):

    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid:
            form.save()
            messages.success(request, 'EVENT UPDATED.')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/eventform.html', context)

# view to delete event
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteEvent(request, pk):
    event = Event.objects.get(id=pk)

    if request.method == 'POST':
        event.delete()
        messages.success(request, 'DELETED')
        return redirect('adminpage')
    context = {'item':event}
    return render(request, 'admindash/delete.html', context)



#+-------------ALL VIEWS FOR ANNOUNCEMENT--------------+
# view for announcement form
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateAnnouncement(request, pk):
    announcement = Announcement.objects.get(id=pk)
    form = AnnouncementForm(instance=announcement)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid:
            form.save()
            messages.success(request, 'ANNOUNCEMENT UPDATED.')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/announcementform.html', context)


# view to delete announcement
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteAnnouncement(request, pk):
    announcement = Announcement.objects.get(id=pk)

    if request.method == 'POST':
        announcement.delete()
        messages.success(request, 'DELETED')
        return redirect('adminpage')
    context = {'item':announcement}
    return render(request, 'admindash/delete.html', context)





#+-------------ALL VIEWS FOR SEED OF WINNING GRACE --------------+

# view for seed of wining grace form
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateSeedofwin(request, pk):
    seedofwin = Seedofwin.objects.get(id=pk)
    form = SeedofwinForm(instance=seedofwin)
    if request.method == 'POST':
        form = SeedofwinForm(request.POST, instance=seedofwin)
        if form.is_valid:
            form.save()
            messages.success(request, 'SEED OF WINNING GRACE UPDATED.')
            return redirect('adminpage')

    context = {'form':form}
    return render(request, 'admindash/seedofwin.html', context)
    

# view to delete sed of winning grace
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteSeedofwin(request, pk):
    seedofwin = Seedofwin.objects.get(id=pk)

    if request.method == 'POST':
        seedofwin.delete()
        messages.success(request, 'DELETED')
        return redirect('adminpage')
    context = {'item':seedofwin}
    return render(request, 'admindash/delete.html', context)





#+-------------ALL VIEWS FOR RECOMMENDED BIBLE VERSE --------------+

# view for recommended bible
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
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
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def updateRecommendedBible(request, pk):
    biblerecom = Recommendedbible.objects.get(id=pk)
    form = BiblerecommendationForm(instance=biblerecom)
    if request.method == 'POST':
        form = BiblerecommendationForm(request.POST, instance=biblerecom)
        if form.is_valid:
            form.save()
            messages.success(request, 'RECOMMENDED BIBLE PASSAGE UPDATED.')
            return redirect('adminpage')
    context = {'form':form}
    return render(request, 'admindash/recommendedbible.html', context)

# view to delete recommended bible verse
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def deleteRecommendedBible(request, pk):
    biblerecom = Recommendedbible.objects.get(id=pk)

    if request.method == 'POST':
        biblerecom.delete()
        messages.success(request, 'DELETED')
        return redirect('adminpage')
    context = {'item':biblerecom}
    return render(request, 'admindash/delete.html', context)
