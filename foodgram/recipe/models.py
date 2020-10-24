from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    dimension = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=50)
    color = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Recipes'
    )
    image = models.ImageField(upload_to='recipe/', blank=True, null=True)
    description = models.TextField()
    cooking_time = models.IntegerField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredients',
        through_fields=('recipe', 'ingredient')
    )
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='Ingredient'
    )
    amount = models.IntegerField()

    def __str__(self):
        return self.ingredient.dimension


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower"
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
        )

    def __str__(self):
        return self.user.username


class FollowRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favor_by'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favor'
    )

    def __str__(self):
        return self.follow_recipe.title


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Shopper'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='Shopping_list'
    )

    def __str__(self):
        return self.recipe.title
