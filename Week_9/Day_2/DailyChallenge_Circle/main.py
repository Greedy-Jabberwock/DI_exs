from math import pi
import turtle


class Circle:
    __circles = []  # (+) make it private

    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius*2
        Circle.add_to_list(self)

    @property
    def circles(self):
        return Circle.__circles

    def calculate_area(self):
        return round(pi * self.radius ** 2, 2)

    def print_circle(self):
        turtle.circle(self.radius)

    @staticmethod
    def add_to_list(cls):
        Circle.__circles.append(cls)

    @staticmethod
    def sort_circles():
        Circle.__circles.sort()

    def __add__(self, other):
        self.radius += other.radius
        return self

    def __gt__(self, other):
        return self.radius > other.radius  # (+) or just return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius  # (+) or just: self.radius == other.radius

    def __repr__(self):
        return f"""Class {self.__class__.__name__},  
               radius: {self.radius},  \
               diameter: {self.diameter}\n"""  # (+) for multiline use """ """

    def __str__(self):
        return f'{self.__class__.__name__} with radius {self.radius}'


c1 = Circle(16)
c2 = Circle(5)
c3 = Circle(1)
print(c2 + c1)
c2 += c3
print(str(c2))
Circle.sort_circles()
print(Circle.circles)
print(c1.calculate_area())
c1.print_circle()
