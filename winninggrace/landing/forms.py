from django.forms import ModelForm
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django import forms
from .models import *


# form for contact page
class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'name':'name',
            'required':'',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter your Name',
        })
        self.fields["email"].widget.attrs.update({
            'name':'email',
            'required':'',
            'type':'text',
            'class':'form-control',
            'placeholder':'Enter your Email',
        })
        self.fields["subject"].widget.attrs.update({
            'name':'subject',
            'required':'',
            'type':'text',
            'class':'form-control',
            'placeholder':'Subject',
        })
        self.fields["message"].widget.attrs.update({
            'name':'message',
            'required':'',
            'type':'text', 
            'class':'form-control',
            'placeholder':'Enter your Message',
        })
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['date_created']