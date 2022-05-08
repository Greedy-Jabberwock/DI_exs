# ============================ Exercise 1 ===============================
print('============================ Exercise 1 ===============================')

class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, new_val):
        self.val = new_val

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val())  # Output: 10
print(MyClass.get_count())                            # Output: 1

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())  # Output: 20
print(MyClass.get_count())                            # Output: 2


# ============================ Exercise 2 ===============================
print('============================ Exercise 2 ===============================')

class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filter_int(val)
        MyClass.count += 1

    @staticmethod
    def filter_int(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val)                # Output: 5
print(b.val)                # Output: 10
print(c.val)                # Output: 15
print(a.filter_int(100))    # Output: 100
