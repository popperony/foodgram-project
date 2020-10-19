from django.core.cache import cache
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import RecipeForm
from .models import Recipe, Ingredient, User, Follow, FollowRecipe, ShoppingList, RecipeIngredients
from .utils import gen_shopping_list, get_ingredients


def index(request):
    tags = request.GET.getlist('filters')
    recipe_list = Recipe.objects.all()
    if tags:
        recipe_list = recipe_list.filter(
            tags__value__in=tags).distinct().all()
    paginator = Paginator(recipe_list, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'index.html',
        {'page': page, 'paginator': paginator, })


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    tags = request.GET.getlist('filters')
    recipe_list = Recipe.objects.filter(author=profile.pk).all()
    if tags:
        recipe_list = recipe_list.filter(tags__value__in=tags)
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html',
            {'profile': profile, 'recipe_list': recipe_list,
            'page': page, 'paginator': paginator, })


@login_required
def new_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST or None, files=request.FILES or None)
        ingredients = get_ingredients(request)
        if not ingredients:
            form.add_error(None, 'Добавьте ингредиенты')
        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            for i in ingredients:
                RecipeIngredients.objects.create(amount=ingredients[i], ingredient=Ingredient.objects.get(ing_name=f'{i}'), recipe=recipe)
            form.save_m2m()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'new_recipe.html', {'form': form})


@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user != recipe.author:
        return redirect('recipes:index')
    if request.method == "POST":
        form = RecipeForm(request.POST or None, files=request.FILES or None, instance=recipe)
        ingredients = get_ingredients(request)
        if form.is_valid():
            FollowRecipe.objects.filter(recipe=recipe).delete()
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            for item in ingredients:
                FollowRecipe.objects.create(
                    units=ingredients[item],
                    ingredient=Ingredient.objects.get(name=f'{item}'),
                    recipe=recipe)
            form.save_m2m()
            return redirect('recipes:index')
    form = RecipeForm(request.POST or None, files=request.FILES or None, instance=recipe)
    return render(request, 'change_recipe.html',
        {'form': form, 'recipe': recipe, })


def recipe_view(request, recipe_id, username):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    profile = get_object_or_404(User, username=username)
    return render(request, 'recipe.html',
        {'profile': profile, 'recipe': recipe, })


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user == recipe.author:
        recipe.delete()
    return redirect('recipes:index')


@login_required
def follow(request, username):
    user = get_object_or_404(User, username=username)
    author_list = Follow.objects.filter(user=user).all()
    paginator = Paginator(author_list, 8)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'follow.html',
        {'page': page, 'paginator': paginator, 'authors':author_list,})


@login_required
def follow_recipe(request, username):
    tags = request.GET.getlist('filters')
    recipe_list = Recipe.objects.filter(author=request.user.id).all()
    if tags:
        recipe_list = recipe_list.filter(
            tags__value__in=tags).distinct()
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'favorite.html',
        {'page': page, 'paginator': paginator, })


def shopping_list(request):
    shopping_list = ShoppingList.objects.filter(user=request.user).all()
    return render(request, 'shopping-list.html', {'shopping_list': shopping_list,})


@login_required
def download(request):
    result = gen_shopping_list(request)
    filename = 'ingredients.txt'
    response = HttpResponse(result, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response
