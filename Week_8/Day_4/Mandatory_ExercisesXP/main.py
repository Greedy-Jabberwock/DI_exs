def print_header(exercise_str):
    border = '---------------------------------------'
    print(f'\n{border}\nExercise {exercise_str}\n')

# ================== Exercise 1: Pets ======================


print_header('1: Pets')


class Pets():

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Britain(Cat):
    def sing(self, sounds):
        return f'{sounds}'


agatha = Britain('Agatha', 4)
perkus = Chartreux('Perkus', 3)
toby = Bengal('Toby', 7)
print(agatha.sing('Mreee.'))
print(perkus.sing('Meooow!'))
print(toby.sing('...!'))
print()
my_cats = [agatha, perkus, toby]
pets_obj = Pets(my_cats)
pets_obj.walk()

# ================== Exercise 2 : Dogs ======================

print_header('2: Dogs')


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking.'

    def get_run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.get_run_speed() * self.weight
        other_power = other_dog.get_run_speed() * other_dog.weight
        winner = self.name if self_power > other_power else other_dog.name
        return f'{winner} wins the fight!'


grizzly = Dog('Grizzly', 3, 7)
grumpy = Dog('Grumpy', 6, 10)
rex = Dog('Rex', 5, 8)
print(grizzly.fight(rex))
print(grizzly.fight(grumpy))
print(rex.fight(grumpy))
print(grumpy.bark())
