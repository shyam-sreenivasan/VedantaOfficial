from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from enum import Enum

class Progress(Enum):
    IN_PROGRESS = 1
    COMPLETED = 2
    NOT_STARTED = 3

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class GroupStatus(Enum):
    ACTIVE = 1
    INACTIVE = 2

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='ACTIVE', choices=GroupStatus.choices())

    def __str__(self):
        return self.group_name

class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user.username, self.group.group_name)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    #image = models.ImageField(upload_to='images/', null=True)
    resource = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.CharField(max_length=200, null=True)
    lesson = models.CharField(max_length=200)
    resource = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.lesson

class GroupCourse(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.group.group_name, self.course.name)

class GroupLesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=Progress.choices(), default='NOT_STARTED')
    date = models.DateField(default='2021-02-18')
    notes = models.CharField(max_length=300, null=True, default='')
    def __str__(self):
        return "{} - {}".format(self.group.group_name, self.lesson.lesson)