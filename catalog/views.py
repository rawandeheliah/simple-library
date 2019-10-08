from django.views import generic

from .models import (Author, Book, BookInstance)


class IndexView(generic.TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        books = Book.objects.select_related('author').all()
        copies = BookInstance.objects
        context['book_count'] = books.count()
        context['copies_count'] = copies.count()
        context['copies_available_count'] = copies.filter(
            status='a').count()
        context['authors_count'] = books.values('author').distinct().count()
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

    def get_context_data(self, *args, **kwargs):
        group_by_value = {}
        context = super(BookDetailView, self).get_context_data(*args, **kwargs)
        context['book'] = self.object
        for j in self.object.languages.all():
            group_by_value[j] = self.object.bookInstances.filter(language=j)

        context['lang'] = group_by_value
        return context


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_info.html'
