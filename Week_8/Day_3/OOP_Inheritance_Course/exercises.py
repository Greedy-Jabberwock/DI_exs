# ======================== EXERCISE 1 ===========================

# class Circle:
#     color = "red"
#
#
# class NewCircle(Circle):
#     color = "blue"
#
#
# nc = NewCircle
# print(nc.color)
# # >> Output will be "blue"

# ======================== EXERCISE 2 ===========================

class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor


class NewCircle(Circle):
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)


nc = NewCircle(1)
print(nc.diameter)

nc.grow()

print(nc.diameter)
# >> Output will be 4

# ======================== EXERCISE 3 ===========================

# This class use superclass name to initialize class A. self argument need to use.
# class A(B):
#     def __init__(self, *args, **kwargs)
#         B.__init__(self, *args, **kwargs)
#         pass
#
# This class use super() function to initialize class A. self argument don't need to be use.
# class A(B):
#     def __init__(self, *args, **kwargs)
#         super().__init__(*args, **kwargs)
#         pass

# =================== EXERCISE 4: Door class ====================


class Door:
    def __init__(self, is_opened):
        self.is_opened = is_opened

    def open_door(self):
        if self.is_opened:
            print('It\'s already opened.')
        else:
            self.is_opened = True

    def close_door(self):
        if self.is_opened:
            self.is_opened = False
        else:
            print("It's already close.")


class BlockedDoor(Door):
    def open_door(self):
        print("ERROR: door can't be opened.")

    def close_door(self):
        print("ERROR: door can't be closed.")


simple_door = Door(True)
simple_door.open_door()
simple_door.close_door()
simple_door.close_door()
blocked = BlockedDoor(False)
blocked.open_door()
blocked.close_door()
