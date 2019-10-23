from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import (PermissionRequiredMixin,
                                        LoginRequiredMixin)

from .models import (Author, Book, BookInstance)
from .forms import (ReserveBookForm, CreateBookForm, CreateAuthorForm)


class IndexView(LoginRequiredMixin, generic.TemplateView):
    login_url = '/accounts/login/'
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


class BookView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Book
    template_name = 'catalog/books_details.html'
    context_object_name = 'bookList'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter().order_by('created_at')


class AuthorView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Author
    template_name = 'catalog/authors_details.html'
    context_object_name = 'authorList'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.filter().order_by('created_at')


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
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

    def form_valid(self, form):

        pass


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Author
    template_name = 'catalog/author_info.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(*args,
                                                                 **kwargs)
        context['author'] = self.object
        return context


class SignUp(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()
        return super(SignUp, self).form_valid(form)


class BookReserveView(LoginRequiredMixin, generic.edit.UpdateView):
    login_url = '/accounts/login/'
    model = BookInstance
    form_class = ReserveBookForm
    success_url = reverse_lazy('catalog:book')
    template_name = 'catalog/reserveBook.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BookReserveView, self).get_context_data(*args,
                                                                **kwargs)
        context['book_language'] = self.request.GET['book_language']
        context['book'] = self.request.GET['book_name']
        context['book_instance'] = self.object
        return context

    def form_valid(self, form):
        book_instance = form.save(commit=False)
        book_instance.borrower = self.request.user
        book_instance.status = 'b'
        book_instance.save()

        return super(BookReserveView, self).form_valid(form)


class BookReserveCompleteView(LoginRequiredMixin, generic.RedirectView):
    login_url = '/accounts/login/'
    template_name = 'catalog/bookReserveCompletion.html'


class CreateBook(PermissionRequiredMixin, generic.edit.CreateView):
    permission_required = 'catalog.can_publish_book'
    model = Book
    form_class = CreateBookForm
    template_name = 'catalog/createBook.html'
    success_url = reverse_lazy('catalog:book')


class CreateAuthor(PermissionRequiredMixin, generic.edit.CreateView):
    permission_required = 'catalog.can_publish_author'
    model = Author
    form_class = CreateAuthorForm
    template_name = 'catalog/createAuthor.html'
    success_url = reverse_lazy('catalog:author')


class SearchResultsView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Book
    template_name = 'catalog/search_results.html'
    context_object_name = 'result_lists'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Book.objects.filter(name__icontains=query)


class BorrowedListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = BookInstance
    template_name = 'catalog/borrowed_results.html'
    context_object_name = 'borrowed_lists'

    def get_queryset(self):
        if self.request.user.has_perm('bookinstance.view_all_instances'):
            return BookInstance.objects.filter(status='b')
        else:
            return BookInstance.objects.filter(borrower=self.request.user)

