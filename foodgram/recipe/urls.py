from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/new/', views.RecipeCreateView.as_view(), name='new-recipe'),
    path('follow/', views.follow, name='follow'),
    path('favorites/', views.favorites, name='favorites'),
    path('shopping-list/', views.shopping_list, name='shopping-list'),
    path('<str:username>/', views.authors_recipes, name='authors-recipes'),
    path('recipes/<int:recipe_id>/edit/', views.RecipeUpdateView.as_view(), name='recipe-edit'),
]
