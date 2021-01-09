from django.http import HttpResponse


def blog(request):
    return HttpResponse("Hello, world. You're at the polls index.")
