# Generated by Django 3.2.10 on 2021-12-31 23:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_remove_property_unique_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='YieldlyToAlgoRatio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('ratio', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
