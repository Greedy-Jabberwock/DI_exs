from re import A


class Farm():

    animals_dict = {}
    
    def __init__(self, name):
        self.name = name
    
    def add_animal(self ,animal_type, count=1):
        animals = self.animals_dict
        if animal_type in animals.keys():
            animals[animal_type] += count
        else:
            animals[animal_type] = count

    def get_animal_types(self):
        return [x for x in self.animals_dict.keys()]

    def get_info(self):
        header = "Old McDonald's farm: \n"
        edges = ('*' * 55) + ('\n')
        info = ''
        animals = self.animals_dict
        line_break = f"*{'_' * (len(edges) - 3)}*\n"
        info += header
        info += edges
        if animals.keys():
            for key, value in animals.items():
                info_values = f'\t{key:<10}:{value:^15}'
                spaces = ' ' * (len(edges) - len(info_values) - 9)
                full_line = f'* {info_values}{spaces}*\n'
                info += full_line + line_break
        else:
            false_info = f'There are no animals at the {self.name}\'s farm yet.'
            false_spaces = ' ' * (len(edges) - len(false_info) - 4)
            full_false_line = f'* {false_info}{false_spaces}*\n'
            info += full_false_line
        info += edges

        return info

    def get_short_info(self):
        types = self.get_animal_types()
        last_el = types[len(types) - 1]
        result = f"{self.name}'s farm has "
        for type in types:
            type_str = f'{type}' if self.animals_dict[type] == 1 else f'{type}s'
            result += f'{type_str}, ' if type != last_el else f'and {type_str}'
        borders = '-' * (len(result) + 4)
        result = f'{borders}\n| {result} |\n{borders}'
        return result

mcdonald = Farm('McDonald')

mcdonald.add_animal('sheep')
mcdonald.add_animal('cow', 2)
mcdonald.add_animal('rabbit', 12)
mcdonald.add_animal('alpaca', 20)
mcdonald.add_animal('horse', 3)

print(mcdonald.get_info())

print(mcdonald.get_short_info())