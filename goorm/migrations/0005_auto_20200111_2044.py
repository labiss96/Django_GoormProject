# Generated by Django 3.0.2 on 2020-01-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goorm', '0004_auto_20200111_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tobacco',
            name='rel_date',
            field=models.CharField(max_length=100),
        ),
    ]