# Generated by Django 4.0 on 2023-03-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_subscriber_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
