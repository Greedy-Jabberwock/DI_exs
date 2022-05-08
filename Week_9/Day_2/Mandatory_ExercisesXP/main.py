def main():
    print_exercise_name('Exercise 1 : Built-In Functions')
    make_exercise_1()
    print_exercise_name('Exercise 2: Currencies')
    make_exercise_2()


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


def make_exercise_1():
    def dopple_abs(number):
        """
        Function to imitate abs() build-in method to get absolute number.
        :param number:
        :return:
        """
        if isinstance(number, (float, int)):
            return number * -1 if number < 0 else number
        else:
            print("Not a number. Return None.")
            return None

    def dopple_int(number=None, base=None):
        """
        Attempt to recreate int() build-in int() method
        :param number:
        :param base:
        :return:
        """
        if number is None:
            return 0
        elif isinstance(number, (int, float)):
            return number.__int__()
        else:
            print(f'{number} is not a number. Return None.')
            return None

    def doppel_input(placeholder):
        """
        Attempt for recreating build-in input() function.
        :param placeholder:
        :return:
        """
        print(placeholder, end='')
        return input()

    x = -5.0
    x = dopple_int(x)
    print(x)
    print(dopple_abs(x))
    print(doppel_input('Print some values: '))


def make_exercise_2():
    class Currency:
        def __init__(self, label, amount):
            self.label = label
            self.amount = amount

        def __int__(self):
            return self.amount.__int__()

        def __str__(self):
            return f'{self.amount} {self.label}{"" if self.amount == 1 else "s"}'

        def __repr__(self):
            return f'{self.amount} {self.label}{"" if self.amount == 1 else "s"}'

        def __add__(self, other):
            try:
                if self.label == other.label:
                    self.amount += other.amount
                    return self
                else:
                    raise TypeError('Labels must be same to add currencies.')
            except TypeError:
                print('TypeError: Currency types must be same to add currencies.')
                return self

    c1 = Currency('shekel', 10)
    c2 = Currency('shekel', 25)
    c3 = Currency('euro', 15)
    c4 = Currency('euro', 3)

    print(c1)
    print(str(c2))
    c1 += c3
    print(c1)
    c1 += c2
    print(c1)
    c4 += c3
    print(c4)


main()
