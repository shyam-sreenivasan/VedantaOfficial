from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView


# Create your views here.

from .forms import CourseForm


def index(request):
    from django.shortcuts import render, redirect
    form = CourseForm(request.POST)
    ctx = {'form': form, 'registered' : False}
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        ctx['registered'] = True
        return render(request, 'courses/index.html', ctx)
    else:
        form = CourseForm()
        ctx['form'] = form
    return render(request, 'courses/index.html', ctx)


# def index(request):
#     course_progress =  Progress.objects.filter(student__username=request.user.username)
#     context = []
#     courses = set()
#     for p in course_progress:
#         course = courses.get(p.course.name, {})
#         course['name'] = p.course.name
#         modules_completed = \
#             course[p.course].get('modules_completed', [])
#         course['modules_completed'] = modules_completed
#         modules_completed.append(p.module)
#         if 'modules' not in course:
#             course['modules'] = Module.objects.filter(course__name=course)
#         courses.add(course)
#
#
#     template = loader.get_template('courses.html')
#     context = {
#         'course_list': '',
#     }
#     return HttpResponse(template.render(context, request))
#
# def detail(request, course_id):
#     return HttpResponse("You're looking at question %s." % course_id)
#
# def results(request, course_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % course_id)
