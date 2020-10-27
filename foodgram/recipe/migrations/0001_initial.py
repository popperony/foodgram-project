# Generated by Django 3.1.2 on 2020-10-27 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название ингредиента')),  # noqa: E501
                ('dimension', models.CharField(blank=True, max_length=255, null=True, verbose_name='Количество')),  # noqa: E501
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('title', models.CharField(max_length=255, verbose_name='Название рецепта')),  # noqa: E501
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe/')),  # noqa: E501
                ('description', models.TextField(verbose_name='Описание')),
                ('cooking_time', models.IntegerField(verbose_name='Время приготовления')),  # noqa: E501
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),  # noqa: E501
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Recipe', to=settings.AUTH_USER_MODEL)),  # noqa: E501
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('name', models.CharField(max_length=255, verbose_name='Имя тега')),  # noqa: E501
                ('value', models.CharField(max_length=50, verbose_name='Значение тега')),  # noqa: E501
                ('color', models.CharField(max_length=30, null=True, verbose_name='цвет')),  # noqa: E501
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_list', to='recipe.recipe')),  # noqa: E501
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopper', to=settings.AUTH_USER_MODEL)),  # noqa: E501
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('amount', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ingredient', to='recipe.ingredient')),  # noqa: E501
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),  # noqa: E501
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe.RecipeIngredients', to='recipe.Ingredient'),  # noqa: E501
        ),
        migrations.AddField(
            model_name='recipe',
            name='tag',
            field=models.ManyToManyField(to='recipe.Tag'),
        ),
        migrations.CreateModel(
            name='FollowRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor', to='recipe.recipe')),  # noqa: E501
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favor_by', to=settings.AUTH_USER_MODEL)),  # noqa: E501
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),  # noqa: E501
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),  # noqa: E501
            ],
        ),
    ]
