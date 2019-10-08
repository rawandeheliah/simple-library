from django.urls import path

from . import views


app_name = 'catalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books/', views.BookView.as_view(), name='book'),
    path('authors/', views.AuthorView.as_view(), name='author'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='bookDetail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(),
         name='authorDetail'),

]
