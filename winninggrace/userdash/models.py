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




# class Prayer(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True)
#     request = models.CharField(max_length=200, null=True, blank=True)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.title)
