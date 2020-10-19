from django import forms

from recipe.models import Ingredient, Recipe, RecipeIngredients, Tag
from django.forms import ModelForm, CheckboxSelectMultiple


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'tags', 'cooking_time', 'description')
        widgets = {'tag': CheckboxSelectMultiple()}
