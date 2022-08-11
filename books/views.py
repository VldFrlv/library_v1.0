from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Q

from books.models import Book


class AddBook(CreateView, LoginRequiredMixin):
    model = Book
    template_name = 'library_managment/add_book.html'
    success_url = reverse_lazy('library_managment:clients')
    fields = [
        'title_rus', 'title_original', 'genre', 'price',
        'authors', 'cover_photo', 'author_photo_1',
        'author_photo_2', 'author_photo_3', 'author_photo_4',
        'price_per_day', 'publication_date', 'num_of_pages'
    ]

@login_required
def group_books(request):
    if not request.user.is_authenticated:
        return reverse_lazy('library_managment:login')
    books = Book.objects.values('title_rus', 'genre', 'publication_date', 'authors', 'num_of_pages')\
        .annotate(all_quantity=Count('title_rus'), av_quantity=Count('title_rus') - Count('title_rus', filter=Q(in_order=True)))
    context = {'books': books}
    return render(request, 'book/group_books.html', context)


class AllBooksList(ListView, LoginRequiredMixin):
    model = Book
    template_name = 'book/all_books.html'
    context_object_name = 'books'

class BookDetail(DetailView, LoginRequiredMixin):
    model = Book
    template_name = 'book/view_book.html'
    context_object_name = 'book'


