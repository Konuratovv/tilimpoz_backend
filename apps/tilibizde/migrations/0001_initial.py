# Generated by Django 4.2.13 on 2024-09-06 20:18

from django.db import migrations, models
import django.db.models.deletion
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tilibizde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='tilibizde/', verbose_name='Сурот')),
                ('title', models.CharField(max_length=200, verbose_name='Аты')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Текст')),
                ('photo2', models.ImageField(upload_to='tilibizde/', verbose_name='Сурот 2')),
                ('description2', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Текст 2')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Тузулгон убактысы')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tilibizde', to='categories.category', verbose_name='Макаланын аты')),
            ],
            options={
                'verbose_name': 'Тилибизде',
                'verbose_name_plural': 'Тилибизде',
            },
        ),
    ]
