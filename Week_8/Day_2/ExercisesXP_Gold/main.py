from math import pi
from random import randint


def print_header(exercise_str):
    border = '\n----------------------------------------------------------------\n'
    print(f'{border}\nExercise {exercise_str}\n')

# ================================ EXERCISE 1: Geometry ========================================


print_header('1: Geometry')


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimetr(self):
        r = self.radius
        return round(2 * r * pi, 3)

    def calculate_area(self):
        r = self.radius
        return pi * r ** 2

    def print_definition(self):
        definition = '''"In Maths or Geometry, a circle is a special kind of ellipse in 
which the eccentricity is zero and the two foci are coincident. A circle is also termed as 
the locus of the points drawn at an equidistant from the centre. The distance from the centre of the 
circle to the outer line is its radius. Diameter is the line which divides the circle into 
two equal parts and is also equal to twice of the radius.
A circle is a basic 2D shape which is measured in terms of its radius. The circles divide 
the plane into two regions such as interior and exterior region. It is similar to the type 
of line segment. Imagine that the line segment is bent around till its ends join. Arrange 
the loop until it is precisely circular.
The circle is a two-dimensional figure, which has its area and perimeter. The perimeter of 
the circle is also called the circumference, which is the distance around the circle. 
The area of the circle is the region bounded by it in a 2D plane. Let us discuss here circle 
definition, formulas, important terms with examples in detail."\n'''
        print('\nCircle definition:\n', definition)


my_circle = Circle(3)
print('\nCircle perimetr:', my_circle.calculate_perimetr())
print('\nCircle area:', my_circle.calculate_area())
my_circle.print_definition()


# ============================= EXERCISE 2 : Custom List Class =================================


print_header('2: Custom List Class')


class MyList:
    def __init__(self, letters):
        self.letters = letters

    def get_reversed_list(self):
        list_to_reverse = self.letters.copy()
        list_to_reverse.reverse()
        return list_to_reverse

    def get_sorted_list(self):
        list_to_sort = self.letters.copy()
        list_to_sort.sort()
        return list_to_sort

    def generate_random_list(self):
        random_list = [randint(0, 100) for _ in range(len(self.letters))]
        return random_list


a_char_index = 97
some_letters = [chr(a_char_index + randint(0, 25)) for x in range(randint(1, 25))]
my_list = MyList(some_letters)
print(my_list.letters)
print(my_list.get_reversed_list())
print(my_list.get_sorted_list())
print(my_list.generate_random_list())




