from django.contrib import admin
from .models import Group,Course, Lesson, \
    GroupMember, GroupCourse, GroupLesson, Testimonial, \
    StoryCatalogue



admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupCourse)
admin.site.register(GroupLesson)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Testimonial)
admin.site.register(StoryCatalogue)
# Register your models here.
