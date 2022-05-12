class Door:
    door_counter = 1
    next_door = None
    KEYS = 3
    _path = ''

    def __init__(self, opened=True):
        self.id = Door.door_counter
        Door.counter_up()
        self.next_door = Door.next_door
        Door.change_next_door(self)
        self.open = opened

    def __repr__(self):
        return f'(id: {self.id}, open: {self.open}, next {self.next})'

    @classmethod
    def counter_up(cls):
        cls.door_counter += 1

    @classmethod
    def change_next_door(cls, door):
        cls.next_door = door

    @property
    def next(self):
        return f'door id: ' \
               f'{self.next_door.id if self.next_door is not None else None}'

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        Door._path = value

    @staticmethod
    def can_go_to(door, other_door):
        cond = door.next_door is None or door is other_door
        if cond:
            Door._path += 'Goal is reached.'
            print(door.path)
            Door._path = ''
            Door.KEYS = 3
            return True
        elif door.id > other_door.id:
            if not door.open and Door.KEYS == 0:
                Door._path += 'No more keys. End of the line.'
                print(door.path)
                return False
            elif not door.open:
                Door._path += f'Used key -> '
                Door.KEYS -= 1
            Door._path += f'Door {door.id} -> '
            return door.can_go_to(door.next_door, other_door)
        else:
            print('Can\'t go')
            return False


d1 = Door(False)
d2 = Door(False)
d3 = Door(False)
d4 = Door(False)
d5 = Door(False)
d6 = Door()
d7 = Door()
Door.can_go_to(d5, d1)