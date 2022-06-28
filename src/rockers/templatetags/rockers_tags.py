from django import template
from rockers.models import *

register = template.Library()

@register.inclusion_tag('rockers/tags/list_roles.html')
def show_roles(sort=None, role_selected=0):
    if not sort:
        roles = Role.objects.all()
    else:
        roles = Role.objects.order_by(sort)

    return {"roles": roles, "role_selected": role_selected}

@register.inclusion_tag('rockers/tags/list_menu.html')
def show_menu():

    menu = [
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Add an article', 'url_name': 'add_article'},
        {'title': 'Feedback', 'url_name': 'feedback'},
    ]

    return {"menu": menu}
