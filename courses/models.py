from django.db import models
from django.contrib.auth.models import User

class Course_Signup(models.Model):
    first_name = models.CharField(max_length=50, help_text='First Name')
    last_name = models.CharField(max_length=50, help_text='Last Name')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, help_text='Phone Number')
#
# class Course(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
#     image = models.ImageField(upload_to='images/')
#
#     def __str__(self):
#         return self.name
#
# class Module(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     name   = models.CharField(max_length=200)
#     description = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.name
#
# class CourseRating(models.Model):
#     rating   = models.IntegerField(default=0)
#     user     = models.ForeignKey(User, on_delete=models.CASCADE)
#     comments = models.CharField(max_length=500)
#     date     = models.DateField()
#
# class MyCourse(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     start_date = models.DateField()
#     votes = models.IntegerField(default=0)
#     status = models.CharField(max_length=50)
#     completion_date = models.DateField(null=True)
#
# class Progress(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     module = models.ForeignKey(Module, on_delete=models.CASCADE)
#     date = models.DateField()
#     comment = models.CharField(max_length=200, null=True)