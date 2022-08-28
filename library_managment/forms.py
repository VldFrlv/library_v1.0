from django import forms
from django.forms import ModelForm

from clients.models import Client
from clients.widget import DatePicketInput
from books.models import Book
from .models import Order


class OrderForm(ModelForm):
    book_queryset = Book.objects.filter(in_order=False)
    book1 = forms.ModelChoiceField(queryset=book_queryset)
    book2 = forms.ModelChoiceField(queryset=book_queryset)
    book3 = forms.ModelChoiceField(queryset=book_queryset)
    book4 = forms.ModelChoiceField(queryset=book_queryset)
    book5 = forms.ModelChoiceField(queryset=book_queryset)

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {'return_date': DatePicketInput}



class SelectClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

