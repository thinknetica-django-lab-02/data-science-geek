import datetime
from urllib.parse import urlparse, parse_qs

from django import template
from requests import Request

from main.models import GoodsCategory, GoodsTag

register = template.Library()


@register.simple_tag
def current_time(format_string: str = '%H:%M') -> str:
    """Возвращает текущее время в указанном формате"""
    now = datetime.datetime.now()
    return now.strftime(format_string)


@register.inclusion_tag('main/snippets/goods_categories_links.html')
def goods_categories_links(html_class: str = 'dropdown-item') -> dict:
    """Возвращает список ссылок с указанным классом <a> на категории товаров """
    categories = GoodsCategory.objects.all()
    return {'categories': categories, 'html_class': html_class}


@register.inclusion_tag('main/snippets/goods_tags_buttons.html', takes_context=True)
def goods_tags_buttons(context) -> dict:
    """Возвращает список ссылок-кнопок <a> на тэги товаров"""
    tags = GoodsTag.objects.all()
    request = context['request']
    return {'tags': tags, 'request': request}


@register.simple_tag
def add_get_params_to_url(value, **kwargs) -> str:
    """Возвращает url-строку с добавленными GET параметрами"""
    url = urlparse(value)
    qs = parse_qs(url.query)
    qs.update(kwargs)

    clear_url = value.split('?')[0] if '?' in value else value
    new_url = Request('GET', clear_url, params=qs).prepare().url
    return str(new_url)
