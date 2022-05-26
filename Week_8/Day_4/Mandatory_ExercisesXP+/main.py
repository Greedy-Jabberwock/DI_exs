def header(func):
    def wrapper(*args, **kwargs):
        print('====================================================================')
        result = func(*args, **kwargs)
        print('====================================================================')
        return result

    return wrapper


@header
def print_exercise_name(exercise_string):
    print(exercise_string)


def main():
    print_exercise_name('Exercise 1: Family')

    class Family:
        def __init__(self, last_name):
            self.members = [
                {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
                {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
            ]
            self.last_name = last_name

        def born(self, **kwargs):
            self.members.append(kwargs)
            print('Congratulate with a new member of family!')

        def is_18(self, name):
            for item in self.members:
                if name == item['name'] and item['age'] >= 18:
                    return True
            else:
                return False

        @property
        def print_family(self):
            result = '\nFamily members:\n--------------------------------------------------\n'
            for member in self.members:
                he_or_she = 'he' if member['gender'].lower() == 'male' else 'she'
                child_str = 'is' if member['is_child'] else "is not"
                result += f'-\t{member["name"]} {self.last_name} is {member["age"]} years old. ' \
                          f'{he_or_she.title()} is a {member["gender"].lower()}, ' \
                          f'and {he_or_she} {child_str} a child.\n' \
                          f'--------------------------------------------------\n'
            return result

    family = Family('Greenberg')
    family.born(name='Jake', age=0, gender='Male', is_child=True)
    print(family.print_family)

    print_exercise_name('Exercise 2: The Incredibles Family')

    class TheIncredibles(Family):
        def __init__(self, last_name):
            super().__init__(last_name)
            self.last_name = last_name
            self.members = [
                {'name': 'Bob', 'age': 35, 'gender': 'Male', 'is_child': False,
                 'power': 'superhuman strength, stamina, and durability',
                 'incredible_name': 'Mr. Incredible'},
                {'name': 'Helen', 'age': 32, 'gender': 'Female', 'is_child': False,
                 'power': 'elastic body',
                 'incredible_name': 'Elastigirl'},
                {'name': 'Dashiell', 'age': 10, 'gender': 'Male', 'is_child': True,
                 'power': 'superhuman speed',
                 'incredible_name': 'Dash'},
                {'name': 'Violet', 'age': 14, 'gender': 'Female', 'is_child': True,
                 'power': 'invisibility',
                 'incredible_name': None}
            ]

        def use_power(self, name):
            if self.is_18(name):
                for i in self.members:
                    if i['name'] == name:
                        print(f'{name.title} use {i["power"]}')
            else:
                raise ValueError

        @property
        def incredible_presentation(self):
            result = '\nFamily members:\n--------------------------------------------------\n'

            for member in self.members:
                he_or_she = 'he' if member['gender'].lower() == 'male' else 'she'
                child_str = 'is' if member['is_child'] else "is not"
                inc_name = 'has no incredible name yet' if member['incredible_name'] is None \
                    else f'is a {member["incredible_name"]}'

                result += f'-\t{member["name"]} {self.last_name} is {member["age"]} years old. ' \
                          f'{he_or_she.title()} is a {member["gender"].lower()}, ' \
                          f'and {he_or_she} {child_str} a child.\n' \
                          f'\t{he_or_she.title()} {inc_name}. ' \
                          f'His power is {member["power"]}.\n' \
                          f'--------------------------------------------------\n'

            return result

    inc_family = TheIncredibles('Parr')
    print(inc_family.print_family)
    inc_family.born(name="Jack-Jack", age=2, gender="Male", is_child=True, power='unknown', incredible_name=None)
    print(inc_family.print_family)
    print(inc_family.incredible_presentation)


main()
