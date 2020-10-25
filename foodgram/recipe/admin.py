from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from recipe.models import (
    FollowRecipe,
    Ingredient,
    Recipe,
    RecipeIngredients,
    ShoppingList,
    Follow,
    Tag
)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredients
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    def count_follow_recipe_now(self, obj):
        return obj.FollowRecipe_set.count()

    count_follow_recipe_now.short_description = 'Counter follow recipe'

    list_display = ('title', 'author', 'pub_date')
    search_fields = ('title', 'author')
    readonly_fields = ('count_follow_recipe_now', 'pub_date')
    empty_value_display = 'None'
    list_filter = ('author', 'title', 'tag')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    inlines = (RecipeIngredientInline,)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'dimension')
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = 'None'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'value')
    empty_value_display = 'None'


@admin.register(Follow)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    empty_value_display = 'None'


@admin.register(RecipeIngredients)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    empty_value_display = 'None'


@admin.register(FollowRecipe)
class FollowRecipeAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    empty_value_display = 'None'


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('pk',)
    empty_value_display = 'None'
