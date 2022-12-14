# Generated by Django 4.0.6 on 2022-08-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('passport', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Hомер паспорта')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес проживания')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
