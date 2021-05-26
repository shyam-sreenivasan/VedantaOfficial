from django.contrib import admin

from .models import Story, StoryReview
# Register your models here.
admin.site.register(Story)
admin.site.register(StoryReview)