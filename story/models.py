from django.db import models

# Create your models here.

class Story(models.Model):
    short_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True)
    date = models.CharField(max_length=250, null=True)
    wished = models.IntegerField()

class StoryReview(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date = models.DateField(default='2021-05-05')
    comment = models.CharField(max_length=2500)
    name = models.CharField(max_length=250)
