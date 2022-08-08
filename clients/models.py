from django.db import models


class Client(models.Model):
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100, blank=True)
    passport = models.CharField('Hомер паспорта',
                                max_length=20,
                                blank=True,
                                unique=True)
    date_of_birth = models.DateField('Дата рождения')
    email = models.EmailField('Email', unique=True)
    address = models.CharField('Адрес проживания', max_length=255)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
