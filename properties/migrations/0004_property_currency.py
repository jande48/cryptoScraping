# Generated by Django 3.2.10 on 2021-12-31 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20211231_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='currency',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
