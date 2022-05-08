"""
Exercise:
    Analyse the code below. What will be the outputs ?

    Explain the goal of the methods
"""


class Circle:
    color = "red"

    def __init__(self, diameter):   # initialize class instance
        self.diameter = diameter

    def grow(self, factor=2):       # upscale the instance
        self.diameter = self.diameter * factor

    def get_color(self):            # return the color attribute of Circle class
        return Circle.color


circle1 = Circle(2)
print(circle1.color)            # Output: red
print(Circle.color)             # Output: red
print(circle1.get_color())      # Output: red
circle1.grow(3)
print(circle1.diameter)         # Output: 6
