from django.contrib import admin

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fieldsets = [
        ('Author Info',                   {'fields': ['name', 'nationality']}),
        ('Author History',                {'fields': ['date_of_birth',
                                                      'date_of_death',
                                                      'place_of_birth']}),
      ]

    def get_date_of_birth_(self, obj):
        if obj:
            return obj.date_of_birth

    def get_date_of_death_(self, obj):
        if obj:
            return obj.date_of_death

    get_date_of_birth_.short_description = "Date of birth"
    get_date_of_death_.short_description = "Date of death"

    list_display = ['name', 'nationality', 'get_date_of_birth_',
                    'get_date_of_death_', 'place_of_birth', 'created_at',
                    'updated_on']
    list_filter = ['place_of_birth', 'nationality']


class LanguageInline(admin.TabularInline):
    model = BookLanguage


class BookLanguageInline(admin.TabularInline):
    model = Language


class GenreInline(admin.TabularInline):
    model = Book.genres.through


class BookAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

    fieldsets = [
        ('Book Info',   {'fields': ('name', 'summary', 'author')}),
    ]
    inlines = [GenreInline, LanguageInline]

    def get_genres(self, obj):
        return ",".join([p.name for p in obj.genres.all()])

    get_genres.short_description = "Geners"
    list_display = ['name', 'summary', 'get_genres', 'author', 'created_at',
                    'updated_on']
    list_filter = ['author__name', 'genres__name']


class LanguageAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'created_at', 'updated_on']


class GenreAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'created_at', 'updated_on']


class BookInstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('BookInstance Info',  {'fields': ('book', 'due_back_date', 'language',
                                           'borrower', 'status')}),
    ]

    def get_book(self, obj):
        if obj:
            return "\n".join([p.name for p in obj.book.all()])

    get_book.short_description = "book"
    list_display = ['status', 'get_book', 'due_back_date', 'created_at',
                    'updated_on', 'language', 'borrower']
    list_filter = ['borrower', 'status', 'language']


admin.site.register(Book, BookAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
