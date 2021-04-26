from django import forms

class CourseSelector(forms.Form):
    course = forms.CharField(label="Stroke", max_length=25, required=True)

class CampRegistration(forms.Form):
    name = forms.CharField(label="name", required=True)
    name = forms.CharField(label="phone", required=True)
    name = forms.CharField(label="email", required=True)
    name = forms.CharField(label="batch", required=True)
    name = forms.CharField(label="timeslot", required=True)