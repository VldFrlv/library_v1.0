from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from books.models import Book


class AddBook(CreateView, LoginRequiredMixin):
    model = Book
    template_name = 'library_managment/add_book.html'
    success_url = reverse_lazy('home')
    fields = [
        'title_rus', 'title_original', 'genre', 'price',
        'authors', 'cover_photo', 'author_photo_1',
        'author_photo_2', 'author_photo_3', 'author_photo_4',
        'price_per_day', 'publication_date', 'num_of_pages'
    ]
