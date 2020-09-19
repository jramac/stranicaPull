from django import template

register = template.Library()

@register.simple_tag
class Counter:
    counter = 0
    def increment(self):
        self.counter += 1
    def set_to_zero(self):
        self.counter = 0