import math


def triangle(base, height):
    """Area of triangle"""
    return base * height / 2


def rectangle(base, height):
    """Area of rectangle"""
    return base * height


def circle(radius):
    """Area of circle"""
    return math.pi * radius ** 2


def donut(outside_radius, inside_radius):
    return circle(outside_radius) - circle(inside_radius)
