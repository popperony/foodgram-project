from .models import ShoppingList
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


def gen_shopping_list(request):
    shopper = get_object_or_404(User, username=request.user.username)
    shopping_list = shopper.shopper.all()
    ingredients = {}
    for item in shopping_list:
        for amount in item.recipe.amount_set.all():
            name = f'{amount.ingredient.title} ({amount.ingredient.dimension})'
            units = amount.units
            if name in ingredients.keys():
                ingredients[name] += units
            else:
                ingredients[name] = units
    result = []
    for key, units in ingredients.item():
        result.append(f'{key} - {units}')
    return result


def get_ingredients(request):
    ingredients = {}
    for key, ingredient_name in request.POST.items():
        if 'nameIngredient' in key:
            _ = key.split('_')
            ingredients[ingredient_name] = int(request.POST[f'valueIngredient_{_[1]}'])
    return ingredients
