# Generated by Django 4.0.6 on 2022-08-05 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('agreement', models.BooleanField(default=True, verbose_name='Пользовательское соглашение')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='clients.client')),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Дата выдачи')),
                ('book1', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='book1', to='books.book', verbose_name='Книга 1')),
                ('book2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book2', to='books.book', verbose_name='Книга 2')),
                ('book3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book3', to='books.book', verbose_name='Книга 3')),
                ('book4', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book4', to='books.book', verbose_name='Книга 4')),
                ('book5', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book5', to='books.book', verbose_name='Книга 5')),
            ],
        ),
    ]
