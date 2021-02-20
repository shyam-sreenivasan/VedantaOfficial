from django import forms

class CourseSelector(forms.Form):
    course = forms.CharField(label="Stroke", max_length=25, required=True)
