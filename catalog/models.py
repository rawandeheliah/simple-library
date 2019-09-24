from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(null=True)
    date_of_death = models.DateTimeField(null=True)
    nationality = models.CharField(max_length=50, blank=True)
    place_of_birth = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "catalog/authors/"


class Genre(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "catalog/books/"


class BookInstance(models.Model):
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {} language'.format(self.book.name, self.language)


