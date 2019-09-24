from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(null=True)
    date_of_death = models.DateTimeField(null=True)
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
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "catalog/books/"


class BookInstance(BaseModel):
    STATUS = (('a', 'available'),
              ('b', 'Reserved'),
              ('m', 'Maintenance'),
              ('ol', 'On Loan'))
    due_back_date = models.DateTimeField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=STATUS,
                              default='Available')
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return '{} : {} language'.format(self.book.name, self.language)
