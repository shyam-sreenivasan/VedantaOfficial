from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
# Create your views here.

from .models import Story, StoryReview

def index(request):
    context = {}
    template = loader.get_template('story/index.html')
    return HttpResponse(template.render(context, request))

def about(request, id):
    from django.db.models import Avg
    story = Story.objects.filter(id=id).first()
    story.max_rating = range(1,6)
    reviews = StoryReview.objects.filter(story__id=id)
    rating = 0
    if len(reviews) > 0:
        rating = int(reviews.aggregate(Avg('rating'))['rating__avg'])

    context = {'story' : story,
               'reviews' : reviews,
               'review_count' : len(reviews),
               'rating' : rating}
    recent = Story.objects.filter(id=1).first()
    rec_reviews = StoryReview.objects.filter(story__id=1)
    if len(rec_reviews) > 0:
        rec_rating = int(rec_reviews.aggregate(Avg('rating'))['rating__avg'])
    context['recent'] = recent
    context['rec_rating'] = rec_rating
    template = loader.get_template('story/about.html')
    return HttpResponse(template.render(context, request))

def review(request, id):
    from .forms import Review
    import datetime
    form = Review(request.POST)
    if form.is_valid():
        rev = StoryReview()
        rev.name = form.data['name']
        rev.rating = form.data['rating']
        rev.comment = form.data['comment']
        rev.date = datetime.datetime.now()
        rev.story = Story.objects.filter(id=id).first()
        rev.save()
    else:
        print ('form not valid {}'.format(form.errors))
    return about(request, id)

