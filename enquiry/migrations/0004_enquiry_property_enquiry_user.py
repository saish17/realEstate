# Generated by Django 4.1.3 on 2022-12-30 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0002_property_bathrooms_property_bedrooms_property_broker_and_more'),
        ('enquiry', '0003_rename_mobile_enquiry_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='property',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='property.property'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enquiry',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
