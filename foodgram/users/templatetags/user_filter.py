from django import template

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


@register.filter
def change_favorite_button(recipe, user_id):
    return recipe.is_favorite(user_id)


@register.filter
def is_in_cart(recipe, user_id):
    return recipe.is_in_cart(user_id)


@register.filter
def is_following(user, author_id):
    return user.following.model.is_following(user, author_id)


@register.filter
def get_filter_values(value):
    return value.getlist('filters')


@register.filter
def get_filter_link(request, tag):
    new_request = request.GET.copy()

    if tag.slug in request.GET.getlist('filters'):
        filters = new_request.getlist('filters')
        filters.remove(tag.slug)
        new_request.setlist('filters', filters)
    else:
        new_request.appendlist('filters', tag.slug)

    return new_request.urlencode()
