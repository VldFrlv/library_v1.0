from django.db import models


class Book(models.Model):
    title_rus = models.CharField('Наименование на русском', max_length=100)
    title_original = models.CharField('Наименование на языке оригинала',
                                      max_length=100,
                                      blank=True)
    genre = models.CharField('Жанр', max_length=50)
    price = models.DecimalField('Стоимость',
                                max_digits=6,
                                decimal_places=2)
    authors = models.CharField('Автор(ы)', max_length=255)
    cover_photo = models.ImageField('Фото обложки', upload_to='media/photo/%Y/%m/%d/')
    author_photo_1 = models.ImageField('Фото автора',
                                       upload_to='media/photo/%Y/%m/%d/',
                                       blank=True)
    author_photo_2 = models.ImageField('Фото автора',
                                       upload_to='media/photo/%Y/%m/%d/',
                                       blank=True)
    author_photo_3 = models.ImageField('Фото автора',
                                       upload_to='media/photo/%Y/%m/%d/',
                                       blank=True)
    author_photo_4 = models.ImageField('Фото автора',
                                       upload_to='media/photo/%Y/%m/%d/',
                                       blank=True)
    price_per_day = models.DecimalField('Цена за день пользования',
                                        max_digits=4,
                                        decimal_places=2)
    publication_date = models.PositiveIntegerField('Год издания')
    register_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    num_of_pages = models.PositiveIntegerField('Количество страниц')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title_rus}'
