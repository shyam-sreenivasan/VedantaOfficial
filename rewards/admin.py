from django.contrib import admin

from .models import MyStroke, Reward, Coach, StudentProgress, Gift,UserGift

admin.site.register(MyStroke)
admin.site.register(Reward)
admin.site.register(Coach)
admin.site.register(StudentProgress)
admin.site.register(Gift)
admin.site.register(UserGift)

# Register your models here.
