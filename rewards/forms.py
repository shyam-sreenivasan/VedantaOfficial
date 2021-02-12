from django import forms
from .models import Stroke, Stroke_labels


class StrokeForm(forms.Form):
    stroke = forms.ChoiceField(label="Stroke", choices=Stroke.choice_labels())
    category = forms.CharField(label='Line 1', max_length=15, required=True)
    action = forms.CharField(label='Line 2', max_length=20, required=True)
    comments = forms.CharField(label='Comments', required=False, max_length=50, widget=forms.Textarea )
    user = forms.CharField(widget=forms.HiddenInput())
    stroker = forms.CharField(label='Your name', max_length=25)