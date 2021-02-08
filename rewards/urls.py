from django.urls import path

from . import views

from . import views
urlpatterns = [
    path('<str:student>/', views.rewards, name='rewards'),
    path('add/<str:student>/', views.add_rewards, name='add rewards'),
    path('', views.rewards, name='rewards'),
]