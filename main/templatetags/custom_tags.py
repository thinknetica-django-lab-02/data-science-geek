import datetime

from django import template

from main.models import GoodsCategory

register = template.Library()


@register.simple_tag
def current_time(format_string='%H:%M'):
    now = datetime.datetime.now()
    return now.strftime(format_string)


@register.inclusion_tag('main/snippets/dropdown_menu_categories.html')
def get_categories():
    categories = GoodsCategory.objects.all()
    return {'categories': categories}
