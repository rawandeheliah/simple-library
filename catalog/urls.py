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
    path('book/<int:pk>/reserve/', views.BookReserveView.as_view(),
         name='bookReserve'),
    path('book/<int:pk>/reserve/completed/',
         views.BookReserveCompleteView.as_view(),
         name='bookReserveComplete'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('books/create/', views.CreateBook.as_view(),
         name='createBook'),
    path('authors/create/', views.CreateAuthor.as_view(),
         name='createAuthor'),
    path('search', views.SearchResultsView.as_view(),
         name='searchBook'),
    path('borrowed/', views.BorrowedListView.as_view(), name='borrowed'),

]
