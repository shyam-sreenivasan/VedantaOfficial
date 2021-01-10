from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import requests
import json
import html
from bs4 import BeautifulSoup

def index(request):
    API_KEY = 'AIzaSyBuRQ2VJSSJxe-ue8g16axeZEcjALEovRU'
    url = 'https://www.googleapis.com/blogger/v3/blogs/638333160983415815/posts/?key={}'.format(API_KEY)
    print ('sending request {}'.format(url))
    response = requests.get(url).text
    d = json.loads(response)
    item0 = d['items'].pop(0)
    posts = []
    for item in d['items']:
        soup = BeautifulSoup(item.get('content'))
        image = soup.findAll('img')[0].get('src')
        posts.append(
            {'image' : image,
             'title' : item.get('title')}
             )
    context = {
        'title' : item0['title'],
        'date' : item0['published'],
        'image' : item0.get('image', {}).get('url', None),
        'content' : item0.get('content', None),
        'posts' : posts
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


# Create your views here.
