from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='story'),
    path('about/<int:id>', views.about, name='about'),
    path('about/<int:id>/rating', views.review, name='about')
]
