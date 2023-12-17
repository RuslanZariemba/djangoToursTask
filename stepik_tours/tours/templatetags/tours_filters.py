from django import template

register = template.Library()


@register.filter(name='make_stars')
def make_stars(stars):
    return f"{int(stars) * '★'}"
