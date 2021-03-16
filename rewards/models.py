from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum

Stroke_labels = {
    'WELLDONE' : 'Well Done',
    'GOODWORK' : 'Good Work',
    'CONGRATULATIONS' : 'Congratulations',
    'YOUROCK' : 'You Rock',
    'BRAVO' : 'Bravo',
    'YOUNAILEDIT' : 'You Nailed it',
    'LOVEIT' : 'Love it',
    'BRILLIANT' : 'Brilliant',
    'AMAZING' : 'Amazing'

}
class Stroke(Enum):
    WELLDONE = 1
    GOODWORK = 2
    CONGRATULATIONS = 3
    YOUROCK = 4
    BRAVO = 5
    YOUNAILEDIT = 6
    LOVEIT = 7
    BRILLIANT = 8
    AMAZING = 9

    @classmethod
    def choice_labels(cls):
        return tuple((i, Stroke_labels[i]) for i in Stroke_labels)

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class MyStroke(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    stroke = models.CharField(max_length=50, choices=Stroke.choices())
    comments = models.CharField(max_length=250, null=True)
    date = models.DateField()

    def __str__(self):
        return self.user.username

class Reward(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stroker = models.CharField(max_length=50, default='Unknown')
    category = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    stroke = models.CharField(max_length=50, choices=Stroke.choices())
    comments = models.CharField(max_length=250, null=True)
    date = models.DateField()
    stroker_fname = models.CharField(max_length=15, default='Unknown')

    def __str__(self):
        return self.user.username

class Coach(models.Model):
    coach = models.CharField(max_length=50)
    student = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.coach
"""
Refrence: https://dev.to/coderasha/create-advanced-user-sign-up-view-in-django-step-by-step-k9m
"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Gift(models.Model):
    name = models.CharField(max_length=25, blank=True)
    collection = models.CharField(max_length=25, blank=True)
    uri = models.CharField(max_length=250, blank=True)
    ref = models.CharField(max_length=250, blank=True)
    attrib = models.CharField(max_length=50, blank=True)
    cost = models.IntegerField(default=10)

class UserGift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, blank=True, null=True)
    collection = models.CharField(max_length=25, blank=True)



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class StudentProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey('mainapp.Lesson', on_delete=models.CASCADE)
    stroke = models.CharField(max_length=50, choices=Stroke.choices())
    date = models.DateField()

    def __str__(self):
        return self.user.username