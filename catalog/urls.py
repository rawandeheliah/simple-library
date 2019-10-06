from django.urls import path

from . import views


app_name = 'catalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books/', views.DetailView.as_view(), name='book'),
    path('authors/', views.DetailView.as_view(), name='author'),
    path('book/<int:pk>/', views.ResultsView.as_view(), name='bookDetail'),
    # ex: /polls/5/vote/
    path('author/<int:pk>/', views.vote, name='authorDetail'),
]
