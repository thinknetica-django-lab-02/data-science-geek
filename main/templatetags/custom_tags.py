import datetime

from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string='%H:%M'):
    now = datetime.datetime.now()
    return now.strftime(format_string)
