from django.urls import path

from . import views
from .views import CourseView
urlpatterns = [
    path('', CourseView.as_view(), name='course'),
]