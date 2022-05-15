class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = str(id_number)
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def __repr__(self):
        family = [x.name for x in self.family]
        return f'{self.name}, {self.id_number}, {self.age}, {self.priority}, ' \
               f'{self.blood_type}, {family}'

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def __repr__(self):
        res = ''
        if not self.is_empty():
            for human in self.humans:
                res += f'{human}\n'
        return res

    def is_empty(self):
        if len(self.humans) == 0:
            print('Queue is empty.')
            return True
        else:
            return False

    def rearrange_queue(self):
        need_arrange = True
        while need_arrange:
            for index, human in enumerate(self.humans):
                try:
                    next = self.humans[index + 1]
                    if next in human.family:
                        need_arrange = True
                        self.swap(next, self.humans[index + 2])
                except IndexError:
                    if index == len(self.humans) -1 and need_arrange:
                        need_arrange = False

    def add_person(self, person):
        temp = []
        if person.age > 60 or person.priority:
            temp.append(person)
        else:
            temp.append(person)
        self.humans = temp + self.humans

    def find_in_queue(self, person):
        if not self.is_empty():
            if person in self.humans:
                for index, human in enumerate(self.humans):
                    if human == person:
                        return index
            else:
                print(f'There is no {person.name} in queue.')

    def swap(self, person1, person2):
        if not self.is_empty():
            p1_index = self.find_in_queue(person1)
            p2_index = self.find_in_queue(person2)
            if p1_index is not None and p2_index is not None:
                self.humans[p1_index] = person2
                self.humans[p2_index] = person1

    def get_next(self):
        if not self.is_empty():
            next = self.humans[0]
            self.humans = self.humans[1:]
            return next
        else:
            return None

    def get_next_blood_type(self, blood_type):
        if not self.is_empty():
            for index, human in enumerate(self.humans):
                if blood_type == human.blood_type:
                    next = human
                    del self.humans[index]
                    return next
        else:
            return None

    def sort_by_age(self):
        older_priority = []
        priority = []
        older = []
        younger = []
        for human in self.humans:
            if human.priority and human.age > 60:
                older_priority.append(human)
            elif human.priority:
                priority.append(human)
            elif human.age > 60:
                older.append(human)
            else:
                younger.append(human)
        self.humans = older_priority + priority + older + younger
        self.rearrange_queue()


def main():
    queue = Queue()
    h1 = Human('12415', 'Victor', 64, False, 'A')
    h2 = Human('25252', 'Seline', 19, True, 'AB')
    h3 = Human('1111', 'Rassell', 23, True, 'O')
    h4 = Human('0052', 'Jenny', 98, True, 'A')
    h5 = Human('2415', 'Arthur', 45, False, 'B')
    h6 = Human('2421', 'Larry', 61, False, 'O')

    h3.add_family_member(h4)
    h3.add_family_member(h6)

    queue.add_person(h1)
    queue.add_person(h2)
    queue.add_person(h3)
    queue.add_person(h4)
    queue.add_person(h5)
    queue.add_person(h6)

    print(queue)
    queue.sort_by_age()
    print(queue)


main()
