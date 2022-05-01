from operator import le


def print_header(exercise_name):
    border = '-----------------------------------------------'
    print(border)
    print(f'Exercise {exercise_name}')


#==================== EXERCISE 1: CATS ==========================

print_header('1: Cats')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def determinate_oldest_cat(*cats_objects):
    largest_age = -1
    for cat in cats_objects:
        if cat.age > largest_age:
            largest_age = cat.age
            oldest = cat
    return oldest


barsik = Cat('Barsik', 6)
grumpy = Cat('Grumpy', 3)
ginger = Cat('Ginger', 5)

oldest_cat = determinate_oldest_cat(barsik, grumpy, ginger)

print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')


#==================== EXERCISE 2 : Dogs ==========================

print_header('2 : Dogs')

class Dog():
    def __init__(self, dog_name, dog_height):
        self.name = dog_name.title()
        self.height = dog_height

    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height * 2}cm height!')

    def __str__(self) -> str:
        return f'This dog named "{self.name}" and it\'s {self.height}cm height.'


davids_dog = Dog('Rex', 50)
print(str(davids_dog))
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(str(sarahs_dog))
sarahs_dog.bark()
sarahs_dog.jump()

who_bigger = davids_dog.name if davids_dog.height > sarahs_dog.height else sarahs_dog.heigth
print('Who is bigger? ', who_bigger)

#==================== EXERCISE 3 : Who’s The Song Producer? ==========================

print_header('3 : Who’s The Song Producer?')

class Song():
    def __init__(self, lyrics = []):
        self.lines = lyrics
    
    def sing_me_a_song(self):
        print()
        for line in self.lines:
            print(line)


stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#==================== EXERCISE 4 : Afternoon At The Zoo ==========================

print_header('4 : Afternoon At The Zoo')

class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal.lower() not in self.animals:
            self.animals.append(new_animal.lower())
            print(f'\n{new_animal.title()} added in the zoo database.')
        else:
            print(f"\nWe already have {new_animal}")

    def get_animals(self):
        species = ', '.join(self.animals)
        print(f'\nThere are next species in the zoo:\n{species}.')

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            index = self.animals.index(animal_sold)
            self.animals.pop(index)
            print(f'\n{animal_sold.title()} removed from zoo\'s database.')
        else:
            print(f'\nWe don\'t have {animal_sold} in zoo database.')
    
    def sort_animals(self):
        self.animals.sort()
        animals = self.animals
        animals_groups = {}
        for animal in animals:
            group = set()
            first_letter = animal[0]
            for animal in animals:
                if animal[0] == first_letter:
                    group.add(animal)
            if first_letter not in animals_groups.keys():
                animals_groups[first_letter] = group
            else:
                continue
        self.sorted_animals = animals_groups


    def get_groups(self):
        print()
        for key, value in self.sorted_animals.items():
            value_str = ', '.join(value)
            print(f'"{key}": {value_str}')

ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animal('Koala')
ramat_gan_safari.add_animal('panda')
ramat_gan_safari.add_animal('lion')
ramat_gan_safari.add_animal('Baboean')
ramat_gan_safari.add_animal('Bold sterch')
ramat_gan_safari.add_animal('Lizard')
ramat_gan_safari.add_animal('Tasmanean devil')
ramat_gan_safari.add_animal('Jaguar')
ramat_gan_safari.add_animal('Leopard')
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.add_animal('owl')
ramat_gan_safari.add_animal('tiger')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
print()
