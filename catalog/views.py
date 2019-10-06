from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Author, Genre, Language, Book, BookInstance
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator


class IndexView(generic.TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['book_count'] = Book.objects.count()
        context['copies_count'] = BookInstance.objects.count()
        context['copies_available_count'] = BookInstance.objects.filter(
            status='a').count()
        context['Authors_count'] = Author.objects.count()
        return context


class BookView(generic.ListView):
    model = Book
    template_name = 'catalog/books_details.html'
    context_object_name = 'bookList'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter().order_by('created_at')


class AuthorView(generic.ListView):
    model = Author
    template_name = 'catalog/authors_details.html'
    context_object_name = 'authorList'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.filter().order_by('created_at')


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_info.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_info.html'
