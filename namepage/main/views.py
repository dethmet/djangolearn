from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Проверка работы</h1>')


def about(request):
    return HttpResponse('<h3>Страница для нас</h3>')


def huyout(request):
    return HttpResponse('<h2>Хуевая страница не для нас</h2>')


def ebout(request):
    return HttpResponse('<h4>Ебаная страница для когото</h4>')
