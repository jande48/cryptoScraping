# Generated by Django 3.2.10 on 2021-12-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='fun_fact',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='code',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='district',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
    ]