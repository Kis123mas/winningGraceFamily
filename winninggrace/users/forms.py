from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *

# form for user creation
class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Enter your username',
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Enter your email address',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
            'id':'fullName'
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Enter your password',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'type':'text',
            'name':'name',
            'class':'form-control',
            'placeholder':'Confirm your password',
        })
    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'password1', 'password2']
        exclude = ['first_name', 'last_name']









# form for registeration

# class UserForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["profile_pic"].widget.attrs.update({
    #         'class':'btn btn-primary btn-sm',
    #         'title':'Upload new profile image',
    #         'class':'bi bi-upload',
    #         'name':'profile_pic'
    #     })
    #     self.fields["firstname"].widget.attrs.update({
    #         'required':'',
    #         'name': 'firtname',
    #         'type':'text',
    #         'class':'form-control',
    #         'id':'fullName'
    #     })
    #     self.fields["middlename"].widget.attrs.update({
    #         'required':'',
    #         'name': 'middlename',
    #         'type':'text',
    #         'class':'form-control',
    #         'id':'fullName'
    #     })
    #     self.fields["lastname"].widget.attrs.update({
    #         'required':'',
    #         'name': 'lastname',
    #         'type':'text',
    #         'class':'form-control',
    #         'id':'fullName'
    #     })
    #     self.fields["username"].widget.attrs.update({
    #         'required':'',
    #         'name': 'username',
    #         'type':'text',
    #         'class':'form-control',
    #         'id':'fullName'
    #     })
    #     self.fields["phone"].widget.attrs.update({
    #         'required':'',
    #         'name': 'phone',
    #         'type':'text',
    #         'class':'form-control',
    #         'id':'fullName'
    #     })
#         self.fields["email"].widget.attrs.update({
#             'required':'',
#             'name': 'email',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["address"].widget.attrs.update({
#             'required':'',
#             'name': 'address',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["state"].widget.attrs.update({
#             'required':'',
#             'name': 'state',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["country"].widget.attrs.update({
#             'required':'',
#             'name': 'country',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["department"].widget.attrs.update({
#             'required':'',
#             'name': 'department',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["twitter_profile"].widget.attrs.update({
#             'required':'',
#             'name': 'twitter_profile',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["facebook_profile"].widget.attrs.update({
#             'required':'',
#             'name': 'facebook_profile',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#         self.fields["instagram_profile"].widget.attrs.update({
#             'required':'',
#             'name': 'instagram_profile',
#             'type':'text',
#             'class':'form-control',
#             'id':'fullName'
#         })
#     class Meta:
#         model = NewUser
#         fields = '__all__'