# hexlet_django_blog/article/views.py

from django.shortcuts import render
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('article')


def index(request):
    app_name = "Hexlet django blog"  # Название приложения
    return render(request, "articles/index.html", {"app_name": app_name})

# Create your views here.
