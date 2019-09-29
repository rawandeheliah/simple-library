from django.contrib import admin
from smart_selects.form_fields import ChainedModelChoiceField
from .models import Author, Book, Language, Genre, BookInstance,BookLanguage


class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fieldsets = [
        (None,                            {'fields': ['name', 'nationality']}),
        ('Author History',                {'fields': ['date_of_birth',
                                                      'date_of_death',
                                                      'place_of_birth']}),
      ]

    def date_of_birth_(self, obj):
        if obj:
            return obj.date_of_birth.date()

    def date_of_death_(self, obj):
        if obj:
            return obj.date_of_death.date()

    list_display = ['name', 'nationality', 'date_of_birth_', 'date_of_death_',
                    'place_of_birth', 'created_at', 'updated_on']
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
        (None,               {'fields': ('name', 'summary', 'author')}),
    ]
    inlines = [GenreInline, LanguageInline]

    def genres_(self, obj):
        return ",".join([p.name for p in obj.genres.all()])

    list_display = ['name', 'summary', 'genres_', 'author', 'created_at',
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
        (None,               {'fields': ('book', 'due_back_date', 'language',
                                         'borrower', 'status')}),
    ]

    def book_(self, obj):
        if obj:
            return  "\n".join([p.name for p in obj.book.all()])
    list_display = ['status', 'book_', 'due_back_date', 'created_at',
                    'updated_on', 'language', 'borrower']
    list_filter = ['borrower', 'status', 'language']


admin.site.register(Book, BookAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
