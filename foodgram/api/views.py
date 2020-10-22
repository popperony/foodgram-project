from django.http import JsonResponse
from django.views.generic import View
from recipe.models import User, Ingredient, Recipe, FollowRecipe, Follow, ShoppingList
from django.shortcuts import get_object_or_404
import json


class Ingredients(View):
    def get(self, request):
        text = request.GET['query']
        ingredients = list(Ingredient.objects.filter(title__icontains=text).values('ing_name', 'dimension'))
        return JsonResponse(ingredients, safe=False)


class Favorites(View):
    def post(self, request):
        recipe_id = json.loads(request.body)['id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        FollowRecipe.objects.get_or_create(user=request.user, follow_recipe=recipe)
        return JsonResponse({'success': True})

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = get_object_or_404(User, username=request.user.username)
        obj = get_object_or_404(FollowRecipe, user=user, recipe=recipe)
        obj.delete()
        return JsonResponse({'success': True})


class Purchases(View):
    def post(self, request):
        recipe_id = json.loads(request.body)['id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        ShoppingList.objects.get_or_create(user=request.user, recipe=recipe)
        return JsonResponse({'success': True})

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        user = get_object_or_404(User, username=request.user.username)
        obj = get_object_or_404(ShoppingList, user=user, recipe=recipe)
        obj.delete()
        return JsonResponse({'success': True})

class Subscription(View):
    def post(self, request):
        author_id = json.loads(request.body)['id']
        author = get_object_or_404(User, id=author_id)
        Follow.objects.get_or_create(
            user=request.user, author=author)
        return JsonResponse({'success': True})

    def delete(self, request, author_id):
        user = get_object_or_404(User, username=request.user.username)
        author = get_object_or_404(User, id=author_id)
        obj = get_object_or_404(Follow, user=user, author=author)
        obj.delete()
        return JsonResponse({'success': True})
