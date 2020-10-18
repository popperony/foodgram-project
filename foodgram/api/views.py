from django.shortcuts import render
from rest_framework import status, viewsets, filters, views
from rest_framework.response import Response
from rest_framework import permissions
from recipe.models import Ingredient, Recipe, FollowRecipe, Follow, ShoppingList


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=following__username', '=user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

