# Generated by Django 4.1 on 2022-08-22 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_forwhom_is_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forwhom',
            name='is_visible',
        ),
    ]
