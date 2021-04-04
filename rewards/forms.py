from django import forms
from .models import Stroke, Stroke_labels
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StrokeForm(forms.Form):
    stroke = forms.ChoiceField(label="Stroke", choices=Stroke.choice_labels())
    category = forms.CharField(label='Line 1', max_length=25, required=True)
    action = forms.CharField(label='Line 2', max_length=25, required=True)
    comments = forms.CharField(label='Comments', required=False, max_length=50, widget=forms.Textarea )
    user = forms.CharField(widget=forms.HiddenInput())
    stroker = forms.CharField(label='Your name', max_length=25)



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

class ClaimGift(forms.Form):
    selectedgift_id = forms.CharField(label='', max_length=25, required=True)

class PracticeLogForm(forms.Form):
    mins = forms.CharField(label='', max_length=25, required=True)