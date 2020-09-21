from django import template

register = template.Library()

counter = 0
@register.simple_tag
def counterr():
    global counter
    counter = counter + 1
    return counter
    
@register.simple_tag
def set_to_zero():
    global counter
    counter = 0
    return counter