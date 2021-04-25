from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ramayana', views.ramayana, name='ramayana'),
    path('ramayana/register', views.register_ramayana, name='register_ramayana'),
    path('manage', views.manage, name='manage'),
    path('manage/<str:group>/', views.manage, name='manage'),
    path('manage/addcourse/<str:group>/', views.add_course, name='addcourse'),
    path('manage/update_lesson_status/<str:group>/<str:lesson>/', views.update_lesson_status),
    path('members/<str:name>/', views.view_member, name='view_member')
]
