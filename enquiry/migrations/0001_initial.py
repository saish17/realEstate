# Generated by Django 4.1.3 on 2022-12-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=13)),
                ('added_date', models.DateField()),
            ],
        ),
    ]