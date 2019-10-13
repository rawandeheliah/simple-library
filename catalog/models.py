from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedManyToManyField
from django.core.exceptions import ValidationError
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    nationality = models.CharField(max_length=50, blank=True)
    place_of_birth = models.CharField(max_length=50, blank=True)

    class Meta:
        permissions = (("v_author", "Can view the author"),
                       ("can_publish_author", "Can publish an author"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "catalog/authors/"


class Genre(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(BaseModel):
    name = models.CharField(max_length=50)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language, through='BookLanguage')

    class Meta:
        permissions = (("v_book", "Can view the book"),
                       ("can_publish_book", "Can publish a book"),)

    def __str__(self):
        return self.name

    def projects(self):
        return self.bookinstance_set()

    def get_absolute_url(self):
        return "catalog/books/"


class BookLanguage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.language.name


class BookInstance(BaseModel):
    STATUS = (('a', 'Available'),
              ('b', 'Reserved'),
              ('m', 'Maintenance'),
              ('ol', 'On Loan'))

    def validate_date(date):
        if date <= timezone.now().date():
            raise ValidationError("Date cannot be in the past or today!")

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    due_back_date = models.DateField(null=True, validators=[validate_date])
    book = ChainedManyToManyField(
        Book,
        horizontal=True,
        verbose_name='book',
        chained_field="language",
        chained_model_field="languages",
        related_name="bookInstances",
    )

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                                 blank=True)
    status = models.CharField(max_length=32, choices=STATUS,
                              default='Available')

    def __str__(self):
        return '{} : {} language'.format(self.book.name, self.language)
