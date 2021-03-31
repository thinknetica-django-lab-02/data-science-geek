import datetime
from urllib.parse import urlparse, parse_qs

from django import template
from requests import Request

from main.models import GoodsCategory, GoodsTag

register = template.Library()


@register.simple_tag
def current_time(format_string='%H:%M'):
    now = datetime.datetime.now()
    return now.strftime(format_string)


@register.inclusion_tag('main/snippets/dropdown_menu_categories.html')
def get_categories():
    categories = GoodsCategory.objects.all()
    return {'categories': categories}


@register.inclusion_tag('main/snippets/tags_cloud.html', takes_context=True)
def get_tags_cloud(context):
    tags = GoodsTag.objects.all()
    request = context['request']
    return {'tags': tags, 'request': request}


@register.simple_tag
def set_get_params(value, **kwargs):
    url = urlparse(value)
    qs = parse_qs(url.query)
    qs.update(kwargs)

    clear_url = value.split('?')[0] if '?' in value else value
    new_url = Request('GET', clear_url, params=qs).prepare().url
    return str(new_url)
