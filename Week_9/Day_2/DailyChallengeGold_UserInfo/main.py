class Person:
    persons = [] # make it private

    def __init__(self, name, age, score):
        if self.valid_info(name, age, score):
            self.info = (str(name).strip(), str(age).strip(), str(score).strip()) # redundant prathenses
            Person.persons.append(self)
            self.validation = True
        else:
            self.validation = False # if it's not validate we need to throw exception
            print('Invalid parameters. Try again.')

    def __repr__(self):
        return f'{self.info}' # it should return info for developers how to create the instance

    def __lt__(self, other):
        for i in range(3):
            if self.info[i] >= other.info[i]:
                return False
        else: # else is redundant 
            return True

    def __le__(self, other):
        for i in range(3):
            if self.info[i] > other.info[i]:
                return False
        else:  # else is redundant 
            return True

    @staticmethod
    def valid_info(name, age, score):
        if str(name).strip().isalpha():
            if str(age).strip().isdigit() and str(score.strip().isdigit()):
                if 0 < int(age) < 120 and 0 < int(score):
                    return True
        else:  # else is redundant 
            return False


def make_person_list():
    i = 0
    while i < 5:
        info_values = input('Enter name, age and score, separated by comma:\n>>> ').split(',')
        try:
            person = Person(*info_values)
        except TypeError:
            print('Invalid input. Try again.')
            continue
        if person.validation:
            i += 1


def main():
    make_person_list()
    persons = Person.persons
    sorted_persons = sorted(persons, key=lambda x: (x.info[0], x.info[1], x.info[2]))
    print(sorted_persons)


main()
