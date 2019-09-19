from django.contrib import admin

from .models import Author, Book, Language, Genre, BookInstance


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(BookInstance)
