# Generated by Django 3.1.2 on 2020-10-24 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20201024_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tags',
            new_name='tag',
        ),
    ]
