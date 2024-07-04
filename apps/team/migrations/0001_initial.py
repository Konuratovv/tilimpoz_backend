# Generated by Django 4.2.13 on 2024-07-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team_images/')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
            ],
        ),
    ]
