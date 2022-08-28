from django.core.exceptions import ValidationError
from django.db import models

from books.models import Book
from clients.models import Client


class Order(models.Model):
    agreement = models.BooleanField('Пользовательское соглашение', default=True)
    client = models.OneToOneField('clients.Client',
                                  on_delete=models.PROTECT,
                                  primary_key=True)
    book1 = models.ForeignKey('books.Book',
                              on_delete=models.PROTECT,
                              verbose_name='Книга 1',
                              related_name='book_1')
    book2 = models.ForeignKey('books.Book',
                              on_delete=models.PROTECT,
                              verbose_name='Книга 2',
                              related_name='book_2',
                              null=True,
                              blank=True)
    book3 = models.ForeignKey('books.Book',
                              on_delete=models.PROTECT,
                              verbose_name='Книга 3',
                              related_name='book_3',
                              null=True,
                              blank=True)
    book4 = models.ForeignKey('books.Book',
                              on_delete=models.PROTECT,
                              verbose_name='Книга 4',
                              related_name='book_4',
                              null=True,
                              blank=True)
    book5 = models.ForeignKey('books.Book',
                              on_delete=models.PROTECT,
                              verbose_name='Книга 5',
                              related_name='book_5',
                              null=True,
                              blank=True)
    order_date = models.DateField('Дата выдачи', auto_now_add=True)
    return_date = models.DateField('Дата возврата')

    def __str__(self):
        return f'Заказ № {self.pk}, клиент: {self.client.name} {self.client.surname} {self.client.patronymic}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'