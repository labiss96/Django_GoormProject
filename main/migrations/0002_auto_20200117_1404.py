# Generated by Django 2.2.7 on 2020-01-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buying_log',
            name='date',
            field=models.DateField(),
        ),
    ]
