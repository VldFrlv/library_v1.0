from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from books.models import Book
from library_managment.forms import OrderForm


class Login(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('library_managment:all_books')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('library_managment:login')


# def change_book_status(save_form):
#     if save_form:
#         book_id = save_form.pk
#         ord_book = Book.objects.get(pk=book_id)
#         ord_book.in_order = True
#         ord_book.save()


@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            print(book.book)
            form.save()
            return redirect('library_managment:all_books')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'library_managment/order.html', context)
