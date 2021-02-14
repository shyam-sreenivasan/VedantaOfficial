from django.urls import path

from . import views

from . import views
urlpatterns = [
    path('<str:student>/', views.rewards, name='rewards'),
    path('add/<str:student>/', views.add_rewards, name='add rewards'),
    path('filter/<str:metric>/', views.filter, name="filter"),
    path('', views.rewards, name='rewards'),

]