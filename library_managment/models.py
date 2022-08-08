from django.db import models

from books.models import Book
from clients.models import Client


class Order(models.Model):
    agreement = models.BooleanField('Пользовательское соглашение', default=True)
    client = models.OneToOneField('clients.Client', on_delete=models.CASCADE, primary_key=True)
    book1 = models.OneToOneField('books.Book',
                                 on_delete=models.PROTECT,
                                 related_name='book1',
                                 verbose_name='Книга 1')
    book2 = models.OneToOneField('books.Book',
                                 on_delete=models.PROTECT,
                                 related_name='book2',
                                 verbose_name='Книга 2',
                                 blank=True,
                                 null=True)
    book3 = models.OneToOneField('books.Book',
                                 on_delete=models.PROTECT,
                                 related_name='book3',
                                 verbose_name='Книга 3',
                                 blank=True,
                                 null=True)
    book4 = models.OneToOneField('books.Book', on_delete=models.PROTECT,
                                 related_name='book4',
                                 verbose_name='Книга 4',
                                 blank=True,
                                 null=True)
    book5 = models.OneToOneField('books.Book',
                                 on_delete=models.PROTECT,
                                 related_name='book5',
                                 verbose_name='Книга 5',
                                 blank=True,
                                 null=True)
    order_date = models.DateField('Дата выдачи', auto_now_add=True)

