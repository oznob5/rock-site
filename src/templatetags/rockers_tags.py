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
