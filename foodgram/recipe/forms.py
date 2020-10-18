from django import forms

from recipe.models import Ingredient, Recipe, RecipeIngredients, Tag


class RecipeCreateOrUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        to_field_name='slug'
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        to_field_name='ing_name'
    )
    amount = {}  # Храним ключ - название ингредиента, значение - его кол-во

    class Meta:
        model = Recipe
        fields = ('title', 'tags', 'ingredients', 'cooking_time', 'description','image')

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()

            for tag in ('breakfast', 'lunch', 'dinner'):
                if tag in data:
                    data.update({'tags': tag})

            index_ingr = 0
            for item in list(data):
                if item.startswith('nameIngredient_'):
                    data.update(
                        {
                            'ingredients': data.get(item),
                        })
                elif item.startswith('valueIngredient_'):
                    self.amount[
                        data.getlist('ingredients')[index_ingr]] = data.get(
                        item)
                    index_ingr += 1

        super().__init__(data=data, *args, **kwargs)

    def save(self, commit=True):
        recipe_obj = super().save(commit=False)

        # Сохраняю поля, кроме ingredients и tags
        recipe_obj.save()

        #  Это для случая, когда редактируешь рецепт,
        #  старые ингредиенты не дублировались.
        #  Они сначала удаляются, а потом записываются новые всем скопом.
        recipe_obj.recipe_ingredients.all().delete()

        # Записываем в связанную сущность RecipeIngredient ингредиенты
        ingredients_amount = self.amount

        recipe_obj.recipe_ingredients.set(
            [
                RecipeIngredient(recipe=recipe_obj, ingredient=ingredient,
                                 amount=ingredients_amount[ingredient.title])
                for ingredient in self.cleaned_data['ingredients']
            ],
            bulk=False)

        # Записываем в связанную сущность Tag_Recipe теги
        recipe_obj.tag.set([tag for tag in self.cleaned_data['tags']])

        # Чтобы значения не дублировались при редактировании
        # (т.к. они сохраняются)
        self.amount = []

        self.save_m2m()
        return recipe_obj