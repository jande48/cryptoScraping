# Generated by Django 3.2.10 on 2021-12-31 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20211231_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent_company',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent_contact',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent_email',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
        migrations.RemoveField(
            model_name='property',
            name='code',
        ),
        migrations.RemoveField(
            model_name='property',
            name='district',
        ),
        migrations.RemoveField(
            model_name='property',
            name='fun_fact',
        ),
        migrations.RemoveField(
            model_name='property',
            name='location',
        ),
        migrations.RemoveField(
            model_name='property',
            name='name',
        ),
        migrations.RemoveField(
            model_name='property',
            name='price',
        ),
        migrations.RemoveField(
            model_name='property',
            name='status',
        ),
        migrations.AddField(
            model_name='property',
            name='data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='unique_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
