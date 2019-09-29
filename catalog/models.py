from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedManyToManyField


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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "catalog/books/"


class BookLanguage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.language.name


class BookInstance(BaseModel):
    STATUS = (('a', 'available'),
              ('b', 'Reserved'),
              ('m', 'Maintenance'),
              ('ol', 'On Loan'))
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    due_back_date = models.DateField(null=True)
    book = ChainedManyToManyField(
        Book,
        horizontal=True,
        verbose_name='book',
        chained_field="language",
        chained_model_field="languages")
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=32, choices=STATUS,
                              default='Available')

    def __str__(self):
        return '{} : {} language'.format(self.book.name, self.language)
