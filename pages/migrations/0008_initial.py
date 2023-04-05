# Generated by Django 4.0 on 2023-03-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0007_delete_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
