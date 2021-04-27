from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import GroupMember
import requests
import json
import html
from django.core import serializers
from bs4 import BeautifulSoup
from .models import GroupLesson, Group, Course, Lesson, Progress
from .forms import CourseSelector

def ramayana(request, context={}):
    template = loader.get_template('mainapp/ramayan.html')
    return HttpResponse(template.render(context, request))

def register_ramayana(request):
    #send email
    from django.core.mail import send_mail
    from vvpsite.settings import EMAIL_HOST_USER
    from .forms import CampRegistration
    form = CampRegistration(request.POST)

    if form.is_valid():
        name = form.data['name']
        phone = form.data['phone']
        email = form.data['email']
        batch = form.data['batch']
        time = form.data['timeslot']
        city = form.data['city']
        subject = 'Camp Registration:{} {} {} {} {} {}'.format(name,phone, email, batch, time, city)
        message = "Name: {}\n Phone: {}\n Email: {}\n Batch: {}\n Time: {}\n City: {}".format(name,phone,email, batch, time, city)
        send_mail(subject,
                  message, EMAIL_HOST_USER, ["vvpeetam@gmail.com"], fail_silently=False)

        context = {'registered' : True}
        return ramayana(request,context)
    else:
        return ramayana(request)

def index(request):
    API_KEY = 'AIzaSyA2NQjAtyZg2qzk3ReDyMw9cYcyglGIp8w'
    url = 'https://www.googleapis.com/blogger/v3/blogs/4014092683200702750/posts/?key={}'.format(API_KEY)
    print ('sending request {}'.format(url))
    response = requests.get(url).text
    d = json.loads(response)
    item0 = d['items'][0]
    posts = []
    max_post = 4
    counter = 0
    for item in d['items']:
        soup = BeautifulSoup(item.get('content'))
        image = soup.findAll('img')[0].get('src')
        posts.append(
            {'image': image,
             'title': item.get('title'),
             'url' : item.get('url')}
        )
        counter += 1
        if counter == max_post:
            break

    context = {
        'title': item0['title'],
        'date': item0['published'],
        'image': item0.get('image', {}).get('url', None),
        'content': item0.get('content', None),
        'posts': posts
    }
    template = loader.get_template('mainapp/index.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'mainapp/index.html')


def manage(request, group=None):
    groups = []
    for g in Group.objects.all():
        grp = {}
        grp['id'] = g.id
        grp['group_label'] = g.group_name
        groups.append(grp)

    sel_group = groups[0] if group is None else \
        Group.objects.filter(id=group).first().__dict__

    print ('sel group is {}'.format(sel_group))
    students = GroupMember.objects.filter(group__id=sel_group['id'])
    s_list = []
    for st in students:
        user = st.user
        s = {}
        s['username'] = user.username
        s['first_name'] = user.first_name
        s['last_name'] = user.last_name
        s_list.append(s)
    courses =[]
    clist = Course.objects.all()
    for c in clist:
        courses.append(c.__dict__['name'])

    context = {'group' : sel_group}
    context['groups'] = groups
    context['courses'] = courses
    context['students'] = s_list
    context['lessons'] = get_lessons(request, sel_group['id'])

    template = loader.get_template('mainapp/manage.html')
    return HttpResponse(template.render(context, request))




def get_lessons(request, grpId):
    l_list = GroupLesson.objects.filter(group__id=grpId)
    lessons = []
    for lesson in l_list:
        l = {}
        l['groupId'] = grpId
        l['course'] = lesson.lesson.course.name
        l['lesson'] = lesson.lesson.lesson
        l['lessonId'] = lesson.lesson.id
        l['module'] = lesson.lesson.module
        l['resource'] = lesson.lesson.resource
        l['status'] = lesson.status
        l['notes'] = lesson.notes
        lessons.append(l)
    return lessons

def add_course(request, group):
    form = CourseSelector(request.POST)
    course = Course.objects.filter(name=form.data['course']).first()
    grp = Group.objects.filter(id=group).first()
    lessons = Lesson.objects.filter(course__name=course)

    for l in lessons:
        old = GroupLesson.objects.filter(group=grp, lesson=l).first()
        if old is not None:
            print ('not adding course as already exists')
            continue
        gl = GroupLesson()
        gl.lesson = l
        gl.group = grp
        gl.save()

    return manage(request,group=group)

def update_lesson_status(request, group, lesson):
    import datetime
    grp = Group.objects.filter(id=group).first()
    l = Lesson.objects.filter(id=lesson).first()
    gl = GroupLesson.objects.filter(group=grp, lesson=l).first()
    gl.status = 'Completed'
    gl.notes = request.POST.get('notes', None)
    gl.date = datetime.datetime.now()
    gl.save()
    return manage(request,group=group)

def view_member(request, name):
    context = {}
    template = loader.get_template('mainapp/aboutme.html')
    return HttpResponse(template.render(context, request))