from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
import requests, json
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Reward, Stroke, Coach, StudentProgress,UserGift, Gift
from .forms import StrokeForm,SignUpForm
from django.views.decorators.http import require_http_methods
from django.apps import apps
from actstream import action
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.shortcuts import redirect

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

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    action.send(request.user, verb="logged in")

@receiver(user_logged_out)
def post_logout(sender, user, request, **kwargs):
    action.send(request.user, verb="logged out")

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
    gmlist = groupMember.objects.filter(user__username=user)
    if gmlist is not None and len(gmlist) > 0:
        print ('number of groups in which {} is member is {}'.format(user,len(gmlist)))
        grplesson = apps.get_model('mainapp', 'GroupLesson')
        all_lessons = []
        for gm in gmlist:
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
            all_lessons.extend(lessons)

        print ('setting lessons as {}'.format(all_lessons))
        strokes['lessons'] = all_lessons
        strokes['toppers'] = get_toppers(gmlist)
    else:
        print ('There are no group membership found for user {}'.format(request.user.username))
    context = strokes
    context['scores'] = []
    try:
        context['toppers'] = strokes['toppers']
        context['scores'] = get_global_scores(user)
        context['gifts'] = get_gifts_for_user(user)
        #print ('toppers is {}'.format(context['toppers']))
    except Exception as e:
        #may get here for first timers, so ignore
        print ('Warning Error {}'.format(e))
        pass

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

def get_global_scores(user):
    from datetime import timedelta
    from django.utils import timezone
    from django.db.models import Count
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    last_month = timezone.now().date() - timedelta(days=30)

    last_wk_score = get_score_for_user(some_day_last_week, user,'Last week', 'tomato')
    last_mnth_score = get_score_for_user(last_month, user, 'Last month', 'green')
    all_time = get_score_for_user(None, user, 'All time', 'blue')

    return [last_wk_score,last_mnth_score,all_time]


def get_score_for_user(date, user, label, color):
    count = 0
    filter = {"user__username" : user}
    if date is not None:
        filter["date__gte"] =  date

    rewards7days = Reward.objects. \
        filter(**filter)
    count = len(rewards7days)

    score = {}
    score['label'] = label
    score['color'] = color
    score['score'] = count * 10
    return score

def get_toppers(grpList):
    gmember = apps.get_model('mainapp', 'GroupMember')
    filter = {"group__group_name__in" : [gm.group.group_name for gm in grpList]}
    members_list = gmember.objects.filter(**filter)
    members = {}
    for m in members_list:
        scores = get_global_scores(m.user.username)
        minfo = members.get(m.user.username, {})
        minfo['fname'] = "{} {}".format(m.user.first_name, m.user.last_name)
        groups =  minfo.get('groups', [])
        if m.group.group_name not in groups:
            groups.append(m.group.group_name)
        minfo['groups'] = groups
        minfo['score'] = scores[2]['score']
        minfo['username'] = m.user.username
        members[m.user.username] = minfo
    return members.values()

def get_gifts_for_user(user):
    gifts = UserGift.objects.filter(user__username=user)
    return gifts

def pick_gift(request):
    gifts = Gift.objects.all()
    score = get_score_for_user(None, request.user.username, 'All time', 'blue')
    spent = UserGift.objects.filter(user=request.user).aggregate(Sum('gift__cost'))
    spent = 0 if spent['gift__cost__sum'] is None else spent['gift__cost__sum']
    balance = score['score'] - spent
    if balance < 0:
        balance = 0

    collections = {}
    for g in gifts:
        coll = collections.get(g.collection, [])
        if coll == []:
            collections[g.collection] = coll
        coll.append(g)


    print ('collections {}'.format(collections))



    context = {'collections': collections, 'balance' : balance}

    print ('context {}'.format(context))
    template = loader.get_template('rewards/gifts-picker.html')
    return HttpResponse(template.render(context, request))


def claim_gift(request):

    from .forms import ClaimGift
    giftform = ClaimGift(request.POST)
    gift = Gift.objects.get(pk=giftform.data['selectedgift_id'])
    print ('selected gift {}'.format(gift.id))
    ug = UserGift()
    ug.user = request.user
    ug.gift = gift
    ug.collection = gift.collection
    ug.save()
    action.send(request.user, verb="claimed Gift {}".format(gift.name))
    return redirect('/rewards')