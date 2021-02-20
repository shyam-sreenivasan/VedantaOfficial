from django.contrib import admin

from .models import MyStroke, Reward, Coach, StudentProgress

admin.site.register(MyStroke)
admin.site.register(Reward)
admin.site.register(Coach)
admin.site.register(StudentProgress)

# Register your models here.
