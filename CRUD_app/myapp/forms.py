from django import forms
from django.forms import fields
from .models import Book
from django.core import validators

class book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name','book_author','book_price']
        widgets = {
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'book_author':forms.TextInput(attrs={'class':'form-control'}),
            'book_price':forms.NumberInput(attrs={'class':'form-control'})
        }
