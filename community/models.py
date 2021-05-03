from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from enum import Enum

class Community(models.Model):
    name  = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    createdat = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class CommunityMember(models.Model):
    comm_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_on = models.DateField()

class Challenge(models.Model):
    comm_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    recurring = models.BooleanField(default=True)
    duration_days = models.IntegerField(default=7)

class CommunityActivity(models.Model):
    comm_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, null=True, default="Created")
    timestamp = models.DateField()

