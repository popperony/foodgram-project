from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple

from recipe.models import Ingredient, Recipe, RecipeIngredients, Tag


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'tag', 'cooking_time', 'description')
        widgets = {'tag': CheckboxSelectMultiple()}
