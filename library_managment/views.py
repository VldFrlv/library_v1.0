from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from books.models import Book
from library_managment.forms import OrderForm
from .models import Order


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
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_managment:all_books')
    else:
        form = OrderForm()
    context = {'form': form}
    return render(request, 'order/order.html', context)


