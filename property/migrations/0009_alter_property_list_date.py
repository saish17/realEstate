# Generated by Django 4.0 on 2023-04-26 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_alter_property_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
