from django.contrib.auth.decorators import login_required
from django.urls import path

from clients.views import CreateClient, Clients
from .views import Login, home, logout, order
from books.views import AddBook

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('home/', home, name='home'),
    path('add/', AddBook.as_view(), name='add_book'),
    path('logout/', logout, name='logout'),
    path('add_client/', CreateClient.as_view(), name='add_client'),
    path('clients/', Clients.as_view(), name='clients'),
    path('order/', order, name='order'),

]

