from django.urls import path

from . import views

from . import views
urlpatterns = [
    path('log_practice/', views.log_practice, name="log_practice"),
    path('pick_gift/', views.pick_gift, name="pick_gift"),
    path('claim_gift', views.claim_gift, name="claim_gift"),
    path('give_stroke/<str:student>/<int:lesson_id>/<str:stroke>/', views.give_stroke, name="stroke"),
    path('signup/', views.signup, name="signup"),
    path('<str:student>/', views.rewards, name='rewards'),
    path('add/<str:student>/', views.add_rewards, name='add rewards'),
    path('filter/<str:metric>/', views.filter, name="filter"),
    path('', views.rewards, name='rewards'),

]