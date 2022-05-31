class Person:
    __persons = []  # make it private

    def __init__(self, name, age, score):
        if self.valid_info(name, age, score):
            self.info = str(name).strip(), str(age).strip(), str(score).strip()  # (+)redundant prathenses
            Person.__persons.append(self)

    def __repr__(self):
        return f"""{self.__class__.__name__}
                    \rName: {self.info[0]} (str)
                    \rAge: {self.info[1]} (int)
                    \rScore: {self.info[2]} (int)"""  # it should return info for developers how to create the instance

    def __str__(self):
        return f'{self.info}'

    def __lt__(self, other):
        for i in range(3):
            if self.info[i] >= other.info[i]:
                return False
        return True  # (+) else is redundant

    def __le__(self, other):
        for i in range(3):
            if self.info[i] > other.info[i]:
                return False
        return True  # (+) else is redundant

    @staticmethod
    def valid_info(name, age, score):
        if str(name).strip().isalpha():
            if str(age).strip().isdigit() and str(score.strip().isdigit()):
                age = int(age)
                score = int(score)
                if 0 < age < 120 and 0 < score:
                    return True
        raise ValueError('Invalid parameters.')  # (+)if it's not validate we need to throw exception

    @classmethod
    def sort_persons(cls):
        persons = Person.__persons
        Person.__persons = sorted(persons, key=lambda x: (x.info[0], x.info[1], x.info[2]))

    @classmethod
    def print_persons(cls):
        for person in cls.__persons:
            print(str(person))


def make_person_list():
    i = 0
    while i < 5:
        info_values = input('Enter name, age and score, separated by comma:\n>>> ').split(',')
        Person(*info_values)
        i += 1
    Person.sort_persons()


def main():
    make_person_list()
    Person.print_persons()


main()
