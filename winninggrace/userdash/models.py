from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.


class Member(models.Model):
    CATEGORY = (
        ('Hebrew Women', 'Hebrew Women'), 
        ('Excellent Men', 'Excellent Men'),
        ('Great Youth', 'Great Youth'),
        ('Eminence Children', 'Eminence Children'),
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="profile2.png", null=True, blank=True)
    firstname = models.CharField(max_length=200, null=True, blank=True)
    middlename = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    twitter_profile = models.CharField(max_length=200, null=True, blank=True)
    facebook_profile = models.CharField(max_length=200, null=True, blank=True)
    instagram_profile = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, choices=CATEGORY, blank=True) 
    date_created = models.DateTimeField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.firstname) + ' | ' + str(self.department)




# model for announcement
class Announcement(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    subject = models.CharField(max_length=155, null=True, blank=True)
    message = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.subject)


# model for program.
class Program(models.Model):
    DEPARTMENT = (
        ('Hebrew Women', 'Hebrew Women'), 
        ('Excellent Men', 'Excellent Men'),
        ('Great Youth', 'Great Youth'),
        ('Eminence Children', 'Eminence Children'),
    )
    title = models.CharField(max_length=155, null=True, blank=True)
    department = models.CharField(max_length=155, choices=DEPARTMENT, null=True, blank=True)
    theme = models.TextField(max_length=5000)
    date = models.DateTimeField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.department) + ' | ' + str(self.theme)


# model for event.
class Event(models.Model):
    pics = models.ImageField(default="profile2.png", null=True, blank=True)
    name = models.CharField(max_length=155, null=True, blank=True)
    title = models.CharField(max_length=5000)
    date = models.DateField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.title)


# model for seed of wininggrace
class Seedofwin(models.Model):
    title = models.CharField(max_length=155, null=True, blank=True)
    bible_verse = models.CharField(max_length=155, null=True, blank=True)
    power_capsule = models.CharField(max_length=155, null=True, blank=True)
    content = models.TextField(max_length=5000, null=True, blank=True)
    bible_reading = models.CharField(max_length=155, null=True, blank=True)
    prayer_bullet = models.CharField(max_length=5000, null=True, blank=True)
    date = models.DateTimeField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.power_capsule)


# model for recommended bible
class Recommendedbible(models.Model):
    verseone = models.CharField(max_length=155, null=True, blank=True)
    versetwo = models.CharField(max_length=155, null=True, blank=True)
    versethree = models.CharField(max_length=155, null=True, blank=True)
    versefour = models.CharField(max_length=5000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.verseone)


class Prayer(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    title = models.CharField(max_length=155, null=True, blank=True)
    content = models.TextField(max_length=155, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.title)