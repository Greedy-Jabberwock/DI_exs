class Farm():
    animals_dict = {} # create it inside the init: self.animals_dict = {} because it's part from the class
    
    def __init__(self, name):
        self.name = name
    
    def add_animal(self, animal_type, count=1):
        animals = self.animals_dict
        if animal_type in animals.keys(): # you can do instead: if animal_type in animals
            animals[animal_type] += count
        else:
            animals[animal_type] = count

    def get_animal_types(self):
        return [x for x in self.animals_dict.keys()]

    def get_info(self): # please rerwite this function it's too complicated 
        header = "Old McDonald's farm: \n"
        edges = ('*' * 30) + '\n'
        info = ''
        animals = self.animals_dict
        line_break = f"{'-' * (len(edges) + 3)}\n"
        info += header
        info += edges
        if animals.keys():
            for key, value in animals.items():
                info_values = f'\t{key:<10}:{value:^15}'
                spaces = ' ' * (round(len(edges) - len(info_values)))
                full_line = f' {spaces}{info_values}{spaces}\n'
                info += full_line + line_break
        else:
            false_info = f'There are no animals at the {self.name}\'s farm yet.'
            false_spaces = ' ' * (len(edges) - len(false_info) )
            full_false_line = f'* {false_info}{false_spaces}*\n'
            info += full_false_line
        info += edges

        return info

    def get_short_info(self):  # please rerwite this function it's too complicated 
        types = self.get_animal_types()
        last_el = types[len(types) - 1]
        result = f"{self.name}'s farm has "
        for _type in types:
            type_str = f'{_type}' if self.animals_dict[_type] == 1 else f'{_type}s'
            result += f'{type_str}, ' if _type != last_el else f'and {type_str}'
        borders = '-' * (len(result) + 7)
        result = f'Short info:\n{borders}\n| {result} |\n{borders}'
        return result


mcdonald = Farm('McDonald')

mcdonald.add_animal('sheep')
mcdonald.add_animal('cow', 2)
mcdonald.add_animal('rabbit', 12)
mcdonald.add_animal('alpaca', 20)
mcdonald.add_animal('horse', 3)

print(mcdonald.get_info())

print(mcdonald.get_short_info())