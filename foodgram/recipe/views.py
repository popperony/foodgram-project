from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from recipe.models import (Recipe, ShoppingList,
                                Follow, Tag, User
)


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipes})