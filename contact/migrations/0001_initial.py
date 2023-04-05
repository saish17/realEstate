# Generated by Django 4.1.3 on 2022-11-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=13)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=100)),
                ('contact_date', models.DateField()),
            ],
        ),
    ]
