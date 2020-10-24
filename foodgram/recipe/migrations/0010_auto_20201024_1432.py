# Generated by Django 3.1.2 on 2020-10-24 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0009_auto_20201024_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followrecipe',
            name='follow_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor', to='recipe.recipe'),  # noqa: E501
        ),
        migrations.AlterField(
            model_name='followrecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor_by', to=settings.AUTH_USER_MODEL),  # noqa: E501
        ),
    ]
