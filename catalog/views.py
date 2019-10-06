from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Author, Genre, Language, Book, BookInstance
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone


class IndexView(generic.DetailView):
    template_name = 'catalog/index.html'
    book_count = Book.objects.count()
    copies_count = BookInstance.objects.count()
    copies_available_count = BookInstance.objects.filter(status='Available')
    Authors_count = Author.objects.count()
    context_object_name = {"book_count": book_count,
                           "copies_count": copies_count,
                           "copies_available_count": copies_available_count,
                           "Authors_count": Authors_count}
