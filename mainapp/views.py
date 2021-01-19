from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json
import html
from bs4 import BeautifulSoup

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
