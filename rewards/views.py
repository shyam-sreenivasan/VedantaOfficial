from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
import requests, json
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Reward, Stroke, Coach, StudentProgress
from .forms import StrokeForm,SignUpForm
from django.views.decorators.http import require_http_methods
from django.apps import apps
from actstream import action
# Create your views here.
STROKE_COLOR = {
    'WELLDONE': '#EAEAEA',
    'GOODWORK': '#CEE2D8',
    'CONGRATULATIONS': '#F8F8E8',
    'YOUROCK': '#DBCAE1',
    'BRAVO': '#E3EAF1',
    'YOUNAILEDIT': '#DBDFED',
    'LOVEIT': '#BFBFDF',
    'BRILLIANT': '#BCC4BC',
    'AMAZING': '#F8EEF2'
}

def rewards(request, student=None, metric=None):
    strokes = {}
    is_coach = False
    user = request.user.username
    # get and populate student list, if user is coach
    studs = Coach.objects.filter(coach=user)
    print ('studs is {}'.format(studs))
    if len(studs) > 0:
        strokes['is_coach'] = True
        is_coach = True
        st_lst = [s.__dict__ for s in studs]
        strokes['students'] = st_lst

    if is_coach:
        user = student if student is not None else \
                    strokes['students'][0]['student']
    else:
        action.send(request.user, verb="logged in")

    if metric is not None:
        reward = Reward.objects.filter(user__username=user, stroke=metric)
    else:
        reward = Reward.objects.filter(user__username=user)

    mystrokes = []
    cat_list = set()
    stats = {}
    for s in reward:
        count = stats.get(s.stroke, 0)
        stats[s.stroke] = count + 1
        stroke = s.__dict__
        stroke['backcolor'] = STROKE_COLOR[s.stroke]
        mystrokes.append(stroke)
        cat_list.add(s.category)

    for i in Stroke:
        if i.name not in strokes:
            strokes[i.name] = 0


    fname = User.objects.get(username=request.user.username)
    first_name = fname.first_name
    first_name = first_name if len(first_name) > 0 else fname
    form = StrokeForm(initial={'stroker' : first_name})

    strokes['strokes'] = mystrokes
    strokes['no_strokes_yet'] = len(mystrokes) == 0
    strokes['selected'] = user
    strokes['form'] = form
    strokes['stats'] = {key : stats[key] if key in stats else 0 for key in STROKE_COLOR}
    strokes['category_list'] = cat_list
    strokes['filter_set'] = metric is not None

    #get the class completed lessons

    groupMember = apps.get_model('mainapp', 'GroupMember')
    gm = groupMember.objects.filter(user__username=user).first()
    if gm is not None:
        grplesson = apps.get_model('mainapp', 'GroupLesson')
        grpLessons = grplesson.objects.filter(group=gm.group, status='Completed')
        lessons = [{'status':grpLson.status,
                    'date': grpLson.date,
                    'course' : grpLson.lesson.course,
                    'module' : grpLson.lesson.module,
                    'lesson' : grpLson.lesson.lesson,
                    'resource': grpLson.lesson.resource,
                    'lessonObj' : grpLson.lesson,

                    'id' : grpLson.lesson.id
                    } for grpLson in grpLessons]
        for l in lessons:
            stud = User.objects.filter(username=user).first()
            p = StudentProgress.objects.filter(lesson=l['lessonObj'], user=stud.id).first()
            if p is not None:
                l['stroke'] = p.stroke

        print ('setting lessons as {}'.format(lessons))
        strokes['lessons'] = lessons
    else:
        print ('There are no group membership found for user {}'.format(request.user.username))
    context = strokes
    if not is_coach:
        context['scores'] = get_global_scores(request)
    else:
        context['scores'] = []

    template = loader.get_template('rewards/index2.html')

    return HttpResponse(template.render(context, request))
    #return render(request, 'rewards/index.html')


def handle_stroke(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StrokeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/stroke/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StrokeForm()

    return render(request, 'index2.html', {'stroke_form': form})

def signup(request):
    from django.shortcuts import render, redirect
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        print ('user form is {}'.format(user.__dict__))
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('rewards')
    return render(request, 'rewards/signup.html', {'form': form})

@require_http_methods(["GET", "POST"])
def filter(request, metric):
    return rewards(request, metric=metric)

@require_http_methods(["POST"])
def add_rewards(request, student):
    import datetime
    print ('Adding rewards to {}'.format(student))
    form = StrokeForm(request.POST)
    # check whether it's valid:

    obj = Reward()
    obj.user = User.objects.filter(username=student)[0]
    obj.category = form.data['category']
    obj.action = form.data['action']
    obj.stroke = form.data['stroke']
    obj.comments = form.data['comments']
    obj.date = datetime.datetime.now()
    obj.stroker = request.user.username
    obj.stroker_fname = form.data['stroker']
    print ('Saving {}'.format(obj.__dict__))
    obj.save()
    # process the data in form.cleaned_data as required
    # ...
    # redirect to a new URL:
    action.send(request.user, verb="assigned gem to {}".format(student))
    return rewards(request, student=student)
    # else:
    #     print ('form is not valid')

def logout_user(request):
    logout(request)

def give_stroke(request, student, lesson_id, stroke):
    import datetime
    lesson = apps.get_model('mainapp', 'Lesson')
    lesson = lesson.objects.filter(id=lesson_id).first()
    user = User.objects.filter(username=student).first()
    sp = StudentProgress()
    sp.lesson = lesson
    sp.stroke = stroke
    sp.user = user
    sp.date = datetime.datetime.now()
    sp.save()

    old = Reward.objects.filter(user__username=student,comments=lesson.lesson,
                          action=lesson.module, category=lesson.course).first()
    if old is None:
        reward = Reward()
        reward.user = user
        reward.stroke = stroke
        reward.category = lesson.course
        reward.action = lesson.module
        reward.comments = lesson.lesson
        reward.stroker = request.user.username
        reward.stroker_fname = User.objects.filter(username=request.user.username).first().first_name
        reward.date = datetime.datetime.now()
        reward.save()
    else:
        print ('this reward is already given')

    return rewards(request, student=student)

def get_global_scores(request):
    from datetime import timedelta
    from django.utils import timezone
    from django.db.models import Count
    some_day_last_week = timezone.now().date() - timedelta(days=7)

    filter = {"date__gte": some_day_last_week}
    rewards7days = Reward.objects.\
        filter(**filter)
    rewards = {}
    for r in rewards7days:
        count = rewards.get(r.user.username, 0)
        count += 1
        rewards[r.user.username] = count

    gmember = apps.get_model('mainapp', 'GroupMember')
    gms = gmember.objects.filter()
    group_score = {}
    members = {}
    user_group = None
    for gm in gms:
        gcount = group_score.get(gm.group.id, 0)
        if gm.user.username in rewards :
            gcount += rewards[gm.user.username]
            group_score[gm.group.id] = gcount
        mcount = members.get(gm.group.id, 0)
        mcount += 1
        members[gm.group.id] = mcount
        if request.user.username == gm.user.username:
            user_group = gm.group.id
    score = {}

    for g in group_score:
        s = int(group_score[g]*10/members[g])
        score[g] = s

    max_score = 0
    for s in score:
        if score[s] > max_score:
            max_score = score[s]

    user = request.user.username
    your_score = {}
    your_score['label'] = 'My score'
    your_score['score'] = (rewards[user] if user in rewards else 0) * 10
    your_score['color'] = 'tomato'

    team_score = {}
    team_score['label'] = 'Team score'
    team_score['score'] = score[user_group]
    team_score['color'] = 'green'

    bteam_score = {}
    bteam_score['label'] = 'Best Team'
    bteam_score['score'] = max_score
    bteam_score['color'] = 'blue'

    scores = [your_score,team_score, bteam_score]
    print ('scores {}'.format(scores))
    return scores