from django import template
from thoughts.forms import ThoughtForm

register = template.Library()

@register.inclusion_tag('thoughts/_form.html')
def thought_form():
    form = ThoughtForm()
    return {'form':form}