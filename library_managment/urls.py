from django.contrib.auth.decorators import login_required
from django.urls import path

from clients.views import CreateClient, Clients
from .views import Login, logout, order, terms_of_use
from books.views import AddBook, group_books, AllBooksList, BookDetail

app_name = 'library_managment'

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('groupe_books/', group_books, name='group_books'),
    path('all_books/', AllBooksList.as_view(), name='all_books'),
    path('add/', AddBook.as_view(), name='add_book'),
    path('logout/', logout, name='logout'),
    path('add_client/', CreateClient.as_view(), name='add_client'),
    path('clients/', Clients.as_view(), name='clients'),
    path('terms_of_use/', terms_of_use, name = 'terms_of_use'),
    path('order/', order, name='order'),
    path('book_detail/<int:pk>', BookDetail.as_view(), name='book_detail')
]

