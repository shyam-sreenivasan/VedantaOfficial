from django.contrib import admin
from django.db import models
from .models import MyStroke, Reward, Coach, StudentProgress, Gift,UserGift

admin.site.register(MyStroke)
admin.site.register(Reward)
admin.site.register(Coach)
admin.site.register(StudentProgress)
# admin.site.register(Gift)
admin.site.register(UserGift)
from django.forms import ModelForm, Textarea

class GiftAdmin(admin.ModelAdmin):
    formfield_overrides = {
    models.TextField: {'widget': Textarea(
                       attrs={'rows': 10,
                              'cols': 100})},
}


# Register your models here.
admin.site.register(Gift, GiftAdmin)