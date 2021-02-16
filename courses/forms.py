from django import forms
from django.forms import ModelForm
from .models import Course_Signup
class CourseForm(ModelForm):
    class Meta:
        model = Course_Signup
        fields = ['first_name', 'last_name', 'email']



