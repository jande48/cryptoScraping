# Generated by Django 3.2.10 on 2021-12-31 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='data',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
