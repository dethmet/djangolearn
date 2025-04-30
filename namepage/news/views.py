from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Ты не смог набросить, что-то сделал не так'
    form = ArticlesForm()
    date = {
        'form': form,
        'error': error
    }


    return render(request, 'news/create.html', date)


def electro(request):
    return render(request, 'news/electro.html')


def developer(request):
    return render(request, 'news/developer.html')


def sociate(request):
    data = {
        'title': 'Самая главная страница!!',
        'values': ['Что-то', 'Еще что-то', 'циферки 123'],
        'obj': {
            'car': 'Жига',
            'age': 30,
            'hobby': 'DotA 2'
        }
    }
    return render(request, 'news/sociate.html', data)