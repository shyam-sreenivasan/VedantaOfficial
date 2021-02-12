from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum
import requests, json
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Reward, Stroke, Coach
from .forms import StrokeForm
from django.views.decorators.http import require_http_methods
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
def rewards(request, student=None):
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
    print ('checking for user {}'.format(user))
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
    context = strokes
    print ('final context is {}'.format(context))
    template = loader.get_template('rewards/index.html')

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

    return render(request, 'index.html', {'stroke_form': form})

@require_http_methods(["GET", "POST"])
def add_rewards(request, student):
    import datetime

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
    obj.save()
    # process the data in form.cleaned_data as required
    # ...
    # redirect to a new URL:
    return HttpResponseRedirect('/rewards')
    # else:
    #     print ('form is not valid')
def logout_user(request):
    logout(request)
