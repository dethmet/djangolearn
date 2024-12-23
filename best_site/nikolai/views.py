from django.http import HttpResponse

def index(request):
    return HttpResponse('Шолом, дорогой друг. Это, таки, лучшая страница в твоей жизни.')
