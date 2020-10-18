from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Ingredient(models.Model):
    ing_name = models.CharField(max_length=255, unique=True)
    dimension = models.CharField(max_length=5)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, null=True, unique=True)
    color = models.CharField(max_length=30, null=True)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Recipes')
    image = models.ImageField(upload_to='recipe/', blank=True, null=True)
    description = models.TextField()
    cooking_time = models.IntegerField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredients')
    tags = models.ManyToManyField(Tag, blank=True)


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField()


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
    def is_following(self, author_id):
        response = Follow.objects.select_related('user', 'author').filter(user=self.id, author=author_id).exists()
        return response


class FollowRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Shopping_list')
