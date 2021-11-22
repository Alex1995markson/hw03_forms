from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='addclass')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})


@register.filter(name="extra_addclass")
def extra_addclass(field, class_attr):
    str_tag = f'<span class="{str(class_attr)}">' + field + '</span>'
    return mark_safe(str_tag)
