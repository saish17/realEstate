# Generated by Django 4.0 on 2023-05-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_propertyphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyphoto',
            name='property',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PropertyPhoto',
        ),
    ]
