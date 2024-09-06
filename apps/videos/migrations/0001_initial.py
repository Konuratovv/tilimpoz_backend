# Generated by Django 4.2.13 on 2024-09-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='videos/')),
                ('youtube_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Кормо',
                'verbose_name_plural': 'Кормолор',
            },
        ),
    ]
