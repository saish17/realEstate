# Generated by Django 4.0 on 2023-05-09 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_alter_city_state_alter_property_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='property.state'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='property.country'),
        ),
    ]
