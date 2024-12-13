from django.shortcuts import render


def index(request):
    data = {
        'title': 'Самая главная страница!!',
        'values': ['Что-то', 'Еще что-то', 'циферки 123'],
        'obj': {
            'car': 'Жига',
            'age': 30,
            'hobby': 'DotA 2'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
