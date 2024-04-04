from django import forms
from django.forms import ModelForm
from .models import Author, Quote

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(ModelForm):
    tags = forms.CharField(label='Tags', max_length=20, required=False) 

    class Meta:
        model = Quote
        fields = ['author', 'tags', 'quote']