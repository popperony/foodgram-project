# Generated by Django 3.1.2 on 2020-10-23 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='dimension',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]