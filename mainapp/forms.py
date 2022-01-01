from django import forms

class CourseSelector(forms.Form):
    course = forms.CharField(label="Stroke", max_length=25, required=True)

class CampRegistration(forms.Form):
    # name = forms.CharField(label="name", required=True)
    phone = forms.CharField(label="phone", required=True)
    email = forms.CharField(label="email", required=True)
    # name = forms.CharField(label="batch", required=True)
    # name = forms.CharField(label="timeslot", required=True)
    # name = forms.CharField(label="city", required=True)

class CampConfirmation(forms.Form):
    name = forms.CharField(label="name", required=True)
    email = forms.CharField(label="email", required=True)
    child = forms.CharField(label="child", required=True)
    grade = forms.CharField(label="grade", required=True)
    city = forms.CharField(label="city", required=True)
    phone = forms.CharField(label="phone", required=True)
    pref = forms.CharField(label="pref", required=True)


class EmailMessage(forms.Form):
    name = forms.CharField(label="name", required=True)
    email = forms.CharField(label="email", required=True)
    subject = forms.CharField(label="subject", required=True)
    content = forms.CharField(label="content", required=True)

class BatchPreference(forms.Form):
    pref = forms.CharField(label="pref", required=True)