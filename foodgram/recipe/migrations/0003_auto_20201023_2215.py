# Generated by Django 3.1.2 on 2020-10-23 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20201023_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ing_name',
            new_name='name',
        ),
    ]