from django.core.exceptions import ValidationError
from django.db import models

from books.models import Book
from clients.models import Client


class Order(models.Model):
    agreement = models.BooleanField('Пользовательское соглашение', default=True)
    client = models.OneToOneField('clients.Client', on_delete=models.CASCADE, primary_key=True)
    book = models.ManyToManyField('books.Book')
    order_date = models.DateField('Дата выдачи', auto_now_add=True)
    return_date = models.DateField('Дата возврата')

    def clean(self, *args, **kwargs):
        if self.book.count() > 5:
            raise ValidationError('Нельзя добавить в заказ больше 5 книг')
        super(Order, self).clean(*args, **kwargs)