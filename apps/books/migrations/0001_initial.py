# Generated by Django 4.2.13 on 2024-08-29 22:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Категориянын аты')),
            ],
            options={
                'verbose_name': 'Китептин категориясы',
                'verbose_name_plural': 'Китептин категориялары',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='books/', verbose_name='Сурот')),
                ('title', models.CharField(max_length=200, verbose_name='Аты')),
                ('description', models.TextField(verbose_name='Баяндалышы')),
                ('file', models.FileField(upload_to='books/', validators=[django.core.validators.FileExtensionValidator(('pdf',))], verbose_name='Китептин файлы')),
                ('year', models.CharField(help_text='Мисалы: 2014', max_length=4, verbose_name='Чыгарылган жылы')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Китеп',
                'verbose_name_plural': 'Китептер',
            },
        ),
    ]
