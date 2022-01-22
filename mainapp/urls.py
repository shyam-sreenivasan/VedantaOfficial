from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ramayana', views.ramayana, name='ramayana'),
    #path('story', views.view_story_dboard, name="story"),
    path('ramayana/register', views.register_ramayana, name='register_ramayana'),
    path('ramayana/confirm', views.confirm_ramayana, name='confirm_ramayana'),
    path('ramayana/buy1', views.buy_page_1, name='buy_ramayana'),
    path('ramayana/buy2', views.buy_page_2, name='buy_ramayana'),
    path('ramayana/thankyou', views.thankyou, name='ramayana_ty'),
    path('ramayana/trial', views.trial, name='ramayana_trial'),
    path('ramayana/send_message', views.send_message, name="send_message"),

    path('manage', views.manage, name='manage'),
    path('manage/<str:group>/', views.manage, name='manage'),
    path('manage/addcourse/<str:group>/', views.add_course, name='addcourse'),
    path('manage/update_lesson_status/<str:group>/<str:lesson>/', views.update_lesson_status),
    path('members/<str:name>/', views.view_member, name='view_member'),

    path('anjay/send_email', views.send_email, name="send_email"),
    path('voice', views.voice_query, name="voice"),
    path('story', views.get_story, name="story"),
    path('catalogue', views.get_movies_catalogue, name="catalogue"),
    path('movie', views.get_movie_details, name="movie")
]
