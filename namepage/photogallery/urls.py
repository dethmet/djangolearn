from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallary_home, name='gallery_home'),
    path('add', views.create, name='add'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete')
]