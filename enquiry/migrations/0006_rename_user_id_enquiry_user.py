# Generated by Django 4.1.3 on 2023-01-24 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0005_rename_user_enquiry_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='user_id',
            new_name='user',
        ),
    ]
