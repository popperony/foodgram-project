# Generated by Django 3.1.2 on 2020-10-23 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20201023_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='value',
            new_name='title',
        ),
    ]
