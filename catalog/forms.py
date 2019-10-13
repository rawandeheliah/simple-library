import datetime

from django import forms

from .models import (BookInstance, Book, Author, Genre, Language)


class ReserveBookForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ('due_back_date',)

    due_back_date = forms.DateField(label="due_back_date?",
                                    widget=forms.SelectDateWidget,
                                    required=True)

    def clean_due_back_date(self):
        date = self.cleaned_data['due_back_date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past "
                                        "or today!")
        return date


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'summary', 'author', 'genres', 'languages')

    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
                                            widget=
                                            forms.CheckboxSelectMultiple)
    languages = forms.ModelMultipleChoiceField(queryset=Language.objects.all(),
                                               widget=
                                               forms.CheckboxSelectMultiple)


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'date_of_birth', 'date_of_death', 'nationality',
                  'place_of_birth')

    YEARS = [x for x in range(1500, 2021)]
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS),
                                    required=True)
    date_of_death = forms.DateField(widget=forms.SelectDateWidget(years=YEARS),
                                    required=True)

    def clean_date_of_death(self):
        date = self.cleaned_data['date_of_death']
        date_of_birth = self.cleaned_data['date_of_birth']
        if date < date_of_birth:
            raise forms.ValidationError("The date of death cannot be before "
                                        "date of birth !!")
        return date
