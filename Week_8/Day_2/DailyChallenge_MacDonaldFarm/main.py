class Farm():

    def __init__(self, name):
        self.name = name
        self.animals_dict = {}  # (+)

    def add_animal(self, animal_type, count=1):
        animals = self.animals_dict
        if animal_type in animals:  # (+)you can do instead: if animal_type in animals
            animals[animal_type] += count
        else:
            animals[animal_type] = count

    def get_animal_types(self):
        return list(self.animals_dict.keys())  # (+) why you do this and not just self.animals_dict.keys()
        # ANSWER: because Python raised an error, that dictionary keys are not subscriptable,
        # i forgot that i just can  use list().

    def get_info(self):  # (+) please rerwite this function it's too complicated
        header = "Old McDonald's farm: \n"
        line_break = "-" * len(header) + '\n'
        info = f'{header}{line_break}'
        animals = self.animals_dict
        if animals.keys():
            for key, value in animals.items():
                info += f'\t{key:<10}:{value:^15}\n {line_break}'
        else:
            info += f'There are no animals at the {self.name}\'s farm yet.'

        return info

    def get_short_info(self):  # (+) please rerwite this function it's too complicated
        types = self.get_animal_types()
        types = [f'{x}s' for x in types]
        result = f"| {self.name}'s farm has " + ", ".join(types) + " |"
        border = '-' * (len(result) + 3)
        result = f'Short info:\n{border}\n{result}\n{border}'
        return result


mcdonald = Farm('McDonald')

mcdonald.add_animal('sheep')
mcdonald.add_animal('cow', 2)
mcdonald.add_animal('rabbit', 12)
mcdonald.add_animal('alpaca', 20)
mcdonald.add_animal('horse', 3)

print(mcdonald.get_info())

print(mcdonald.get_short_info())
