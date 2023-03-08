# example custom tag function
import random

from django import template
from home.models import Car

register = template.Library()

@register.simple_tag
def random_car():
    cars = Car.objects.all()
    random_index = random.randint(0, len(cars)-1)
    return cars[random_index].brand

@register.simple_tag
def custom_date_format(date):
    return date.strftime('%Y-%m-%d')

@register.filter(name='foo')
def foo(value):
    """do something to value"""
    value += 100
    return value

@register.filter(name='boo')
def boo(value, other_value):
    """do something to value"""
    return value * int(other_value)

@register.filter(name='zoo')
def zoo(value, other_value):
    """do something to value"""
    val_list = other_value.split(",")
    val_list = [int(x) for x in val_list]
    return value * sum(val_list)