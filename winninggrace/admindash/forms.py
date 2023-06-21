from django.forms import ModelForm
from django.conf import settings
from userdash.models import *

# form for Announcement
class AnnouncementForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'required':'',
            'name': 'lastname',
            'type':'text',
            'class':'form-control',
        })
        self.fields["subject"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
        })
        self.fields["message"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
    class Meta:
        model = Announcement
        fields = '__all__'
        exclude = ['created']

    
# form for Event
class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'required':'',
            'name': 'name',
            'type':'text',
            'class':'form-control',
        })
        self.fields["title"].widget.attrs.update({
            'required':'',
            'name': 'phone',
            'type':'text',
            'class':'form-control',
        })
        self.fields["date"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
    class Meta:
        model = Event
        fields = '__all__'


# form for Program
class ProgramForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            'required':'',
            'name': 'lastname',
            'type':'text',
            'class':'form-control',
        })
        self.fields["department"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-select',
        })
        self.fields["theme"].widget.attrs.update({
            'required':'',
            'name': 'phone',
            'type':'text',
            'class':'form-control',
        })
        self.fields["date"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
    class Meta:
        model = Program
        fields = '__all__'


# form for Seed of winninggrace
class SeedofwinForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({
            'required':'',
            'name': 'lastname',
            'type':'text',
            'class':'form-control',
        })
        self.fields["bible_verse"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
        })
        self.fields["power_capsule"].widget.attrs.update({
            'required':'',
            'name': 'phone',
            'type':'text',
            'class':'form-control',
        })
        self.fields["content"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
        self.fields["bible_reading"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
        self.fields["prayer_bullet"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
        self.fields["date"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
    class Meta:
        model = Seedofwin
        fields = '__all__'



# form for bible recommendation
class BiblerecommendationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["verseone"].widget.attrs.update({
            'required':'',
            'type':'text',
            'class':'form-control',
        })
        self.fields["versetwo"].widget.attrs.update({
            'required':'',
            'name': 'username',
            'type':'text',
            'class':'form-control',
        })
        self.fields["versethree"].widget.attrs.update({
            'required':'',
            'type':'text',
            'class':'form-control',
        })
        self.fields["versefour"].widget.attrs.update({
            'required':'',
            'name': 'department',
            'type':'text',
            'class':'form-control',
        })
    class Meta:
        model = Recommendedbible
        fields = '__all__'