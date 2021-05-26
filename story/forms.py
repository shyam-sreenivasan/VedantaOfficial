from django import forms

class Review(forms.Form):
    name = forms.CharField(label='name', max_length=250, required=True)
    comment = forms.CharField(label='comment', max_length=250, required=True)
    rating = forms.CharField(label="rating", required=True)