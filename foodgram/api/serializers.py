from recipe.models import Ingredient, Recipe, FollowRecipe, Follow, ShoppingList
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    following = serializers.SlugRelatedField(
        read_only=False,
        queryset=User.objects.all(),
        slug_field='username'
        )

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

    def validate(self, value):
        following = value['following']
        user = self.context['request'].user
        follows = Follow.objects.filter(user=user, following=following)
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
        f"Вы уже подписаны на автора {following}"
            )
        return value


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('ing_name', 'dimension')
        model = Ingredient
