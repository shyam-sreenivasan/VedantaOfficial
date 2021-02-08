from django.db import models
from django.contrib.auth.models import User
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

class Reward(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    stroke = models.CharField(max_length=50, choices=Stroke.choices())
    comments = models.CharField(max_length=250, null=True)
    date = models.DateField()

class Coach(models.Model):
    coach = models.CharField(max_length=50)
    student = models.CharField(max_length=50)
    date = models.DateField()
