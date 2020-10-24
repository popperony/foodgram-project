from django import template
from django.http import QueryDict
from recipe.models import Recipe, Tag, FollowRecipe, ShoppingList, Follow


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='rupluralize')
def rupluralize(value, arg="комментарий,комментария,комментариев"):
    args = arg.split(",")
    number = abs(int(value))
    a = number % 10
    b = number % 100
    if (a == 1) and (b != 11):
        return args[0]
    elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
        return args[1]
    else:
        return args[2]


@register.filter(name='get_filter_values')
def get_filter_values(value):
    return value.getlist('filters')

@register.filter(name='get_filter_link')
def get_filter_link(request, tag):
    new_request = request.GET.copy()
    if tag.value in request.GET.getlist('filters'):
        filters = new_request.getlist('filters')
        filters.remove(tag.value)
        new_request.setlist('filters', filters)
    else:
        new_request.appendlist('filters', tag.value)
    return new_request.urlencode()


@register.filter(name='is_favorite')
def is_favorite(recipe, user):
    return FollowRecipe.objects.filter(user=user, recipe=recipe).exists()
    #return True

@register.filter(name='is_shop')
def is_shop(recipe, user):
    return ShoppingList.objects.filter(user=user, recipe=recipe).exists()


@register.filter(name='is_follow')
def is_follow(author, user):
    return Follow.objects.filter(user=user, author=author).exists()
