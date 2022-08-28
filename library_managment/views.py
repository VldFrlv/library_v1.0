from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from books.models import Book
from clients.models import Client
from library_managment.forms import OrderForm
from .utils import *


class Login(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('library_managment:all_books')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('library_managment:login')


@login_required
def terms_of_use(request):
    return render(request, 'library_managment/terms_of_use.html')


@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            for book in (book.book1, book.book2, book.book3, book.book4, book.book5):
                if book:
                    change_book_status(book)
            form.save()
            return redirect('library_managment:all_books')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'library_managment/order.html', context)
