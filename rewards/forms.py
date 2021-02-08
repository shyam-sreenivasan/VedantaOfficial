from django import forms
from .models import Stroke, Stroke_labels


class StrokeForm(forms.Form):
    stroke = forms.ChoiceField(label="Stroke", choices=Stroke.choice_labels())
    category = forms.CharField(label='Category', max_length=50, required=True)
    action = forms.CharField(label='Action', max_length=50, required=True)
    comments = forms.CharField(label='Comments', max_length=50, widget=forms.Textarea )
    user = forms.CharField(widget=forms.HiddenInput())