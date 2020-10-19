from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('ingredients/', views.Ingredients.as_view(), name='ingredients'),
    path('favorites/', views.Favorites.as_view(), name='add_favor'),
    path('favorites/<int:recipe_id>/', views.Favorites.as_view(), name='remove_favor'),
    path('subscriptions/', views.Subscription.as_view(), name='add_subs'),
    path('subscriptions/<int:author_id>/', views.Subscription.as_view(), name='remove_subs'),
    path('purchpurchases/', views.Purchpurchases.as_view(), name='add_to_shop'),
    path('purchpurchases/<int:recipe_id>/', views.Purchpurchases.as_view(), name='remove_from_shop'),
]
