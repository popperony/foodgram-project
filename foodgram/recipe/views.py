from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from recipe.forms import RecipeCreateOrUpdateForm
from recipe.models import (Recipe, ShoppingList,
                                Follow, Tag, User
)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateOrUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'recipe-new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeCreateOrUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'recipe-edit.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect('index')
        return super(RecipeUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        recipe_id = self.kwargs.get('recipe_id')
        return get_object_or_404(Recipe, pk=recipe_id)


def index(request):
    recipes_list = Recipe.objects.select_related(
        'author'
    ).prefetch_related(
        'tag',
    )

    # Проверяем фильтрацию по тегам
    filters = request.GET.getlist('filters')
    if filters:
        recipes_list = Recipe.objects.filter(
            tag__slug__in=filters).distinct()

    all_tags = Tag.objects.all()

    paginator = Paginator(recipes_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'paginator': paginator,
        'all_tags': all_tags,
    }

    return render(request, 'index.html', context=context)


def authors_recipes(request, username):
    author = get_object_or_404(User, username=username)

    recipes = author.Recipes.all()

    # Проверяем фильтрацию по тегам
    filters = request.GET.getlist('filters')
    if filters:
        recipes = Recipe.objects.filter(
            tag__slug__in=filters, author=author).distinct()

    all_tags = Tag.objects.all()

    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'paginator': paginator,
        'author': author,
        'all_tags': all_tags
    }

    return render(request, 'authors_recipes.html', context=context)


@login_required
def favorites(request):
    user = get_object_or_404(User, username=request.user)
    recipes_list = FavoritesRecipes.objects.prefetch_related(
        'favorites__tag', 'favorites__author'
    ).filter(
        user=user)

    # Проверяем фильтрацию по тегам
    filters = request.GET.getlist('filters')
    if filters:
        recipes_list = FavoritesRecipes.objects.filter(
            favorites__tag__slug__in=filters, user=user).distinct()

    all_tags = Tag.objects.all()

    paginator = Paginator(recipes_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'paginator': paginator,
        'all_tags': all_tags,

    }
    return render(request, 'favorites.html', context=context)


@login_required
def shopping_list(request):
    recipe_shopping_list = ShoppingList.objects.select_related('recipe').filter(user=request.user.id)
    context = {'shopping_list': recipe_shopping_list,}
    return render(request, 'shopping-list.html', context=context)


@login_required
def follow(request):
    following = Follow.objects.select_related(
        'user', 'author'
    ).filter(
        user=request.user
    )
    paginator = Paginator(following, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
    }

    return render(request, 'follow.html', context=context)