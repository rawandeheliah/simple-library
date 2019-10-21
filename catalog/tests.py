import datetime


from django.contrib.auth.models import (User, Permission)
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.test import Client


from .forms import CreateAuthorForm, ReserveBookForm
from .models import (Author, Book, Genre, Language, BookInstance)


class MyTests(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create(username='johnsnow')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='johnsnow', password='12345')
        self.author1 = Author.objects.create(name='Mahmoud Darwish',
                                             date_of_birth=datetime.date(1941, 3, 31),
                                             date_of_death=datetime.date(2008, 8, 9),
                                             nationality='Palestinian',
                                             place_of_birth='Palestine')
        self.author1.save()
        self.author2 = Author.objects.create(name='Ghasan Kanfani',
                                             date_of_birth=datetime.date(1936, 3, 31),
                                             date_of_death=datetime.date(1976, 7, 9),
                                             nationality='Palestinian',
                                             place_of_birth='Palestine')
        self.author2.save()
        self.genre = Genre.objects.create(name='drama')
        self.genre.save()
        self.language = Language.objects.create(name='Arabic')
        self.language.save()
        self.book1 = Book.objects.create(name='bortqal yafa',
                                         summary='summary',
                                         author=self.author2)
        self.book1.genres.add(self.genre)
        self.book1.languages.add(self.language)
        self.book1.save()
        self.book2 = Book.objects.create(name='book1',
                                         summary='summary',
                                         author=self.author1)
        self.book2.genres.add(self.genre)
        self.book2.languages.add(self.language)

        self.book2.save()
        self.book_ins = BookInstance.objects.create(status='a',
                                                    language=self.language,
                                                    due_back_date=datetime.date.today() + datetime.timedelta(days=1),
                                                    borrower=self.user,
                                                    )
        self.book_ins.book.add(self.book1)
        self.book_ins.save()

    def test_author_list(self):
        response = self.client.get('/catalog/authors/')
        author_list = response.context['authorList']
        self.assertEqual(len(author_list), 2)

    def test_author_detali_view(self):
        obj_id = self.author1.id
        url = '/catalog/author/{}/'.format(obj_id)
        response = self.client.get(url)
        self.assertEqual(response.context['author'].name, 'Mahmoud Darwish')

    def test_book_list(self):
        response = self.client.get('/catalog/books/')
        author_list = response.context['bookList']
        self.assertEqual(len(author_list), 2)

    def test_book_detali_view(self):
        obj_id = self.book2.id
        url = '/catalog/book/{}/'.format(obj_id)
        response = self.client.get(url)
        self.assertEqual(response.context['book'].summary, 'summary')

    def test_admin_permissions_author_creation(self):
        content_type = ContentType.objects.get_for_model(Author)
        permission = Permission.objects.get(content_type=content_type, codename='can_publish_author')

        admin_user = User.objects.create(username='cersei', is_staff=True)
        admin_user.set_password('12345')
        admin_user.save()
        admin_user.user_permissions.add(permission)

        client = Client()
        client.login(username='cersei', password='12345')

        response = client.get('/catalog/authors/create/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(user.has_perm('catalog.can_publish_author'), True)

    def test_user_permissions_author_creation(self):
        response = self.client.get('/catalog/authors/create/')
        self.assertEqual(response.status_code, 403)

    def test_admin_permissions_book_creation(self):
        content_type = ContentType.objects.get_for_model(Book)
        permission = Permission.objects.get(content_type=content_type,
                                            codename='can_publish_book')

        admin_user = User.objects.create(username='cersei', is_staff=True)
        admin_user.set_password('12345')
        admin_user.save()
        admin_user.user_permissions.add(permission)

        client = Client()
        client.login(username='cersei', password='12345')

        response = client.get('/catalog/books/create/')
        self.assertEqual(response.status_code, 200)
        # worked  self.assertEqual(user.has_perm('catalog.can_publish_author'), True)

    def test_form_submitting_author(self):
        form_data = {'name': 'new_book',
                     'date_of_birth': datetime.date(1941, 3, 1),
                     'date_of_death': datetime.date(2000, 3, 31),
                     'nationality': 'Lebanese',
                     'place_of_birth': 'Beirut',
                     }
        form = CreateAuthorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_book_reservation(self):
        book_id = self.book_ins.id
        url = '/catalog/book/{}/reserve/?book_id={}&book_name={}&book_language' \
              '={}&language_id={}'.format(book_id, self.book1.id,
                                          self.book1.name, self.language,
                                          self.language.id)
        response = self.client.get(url)
        form = response.context['form']
        self.assertIsInstance(form, ReserveBookForm)

    def test_reserveed_book_ins(self):
        self.book_ins.status = 'b'
        self.book_ins.save()

        book_id = self.book_ins.id
        url = '/catalog/book/{}/reserve/?book_id={}&book_name={}&book_language' \
              '={}&language_id={}'.format(book_id, self.book1.id,
                                          self.book1.name, self.language,
                                          self.language.id)
        response = self.client.get(url)
        self.assertContains(response, '<h1> You can\'t reserve this copy ! SORRY! but it is unavailable !</h1>')
