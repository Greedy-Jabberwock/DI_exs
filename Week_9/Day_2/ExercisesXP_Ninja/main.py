def header(exercise_str):
    def wrapper(fn):
        def inner_wrapper(*args, **kwargs):
            border = '=' * 60
            print(border)
            print(f'Exercise {exercise_str}:\n')
            fn(*args, **kwargs)
            print(border)

        return inner_wrapper

    return wrapper


def main():
    make_exersice_1()
    make_exercise_2()


@header('1: Temperature')
def make_exersice_1():
    class Temperature:
        def __init__(self, degree):
            self.degree = degree

    class Celsius(Temperature):
        def __init__(self, degree):
            super().__init__(degree)
            self.name = 'C'

        def to_fahrenheit(self):
            return round(self.degree * (9 / 5) + 32, 1)

        def to_kelvin(self):
            return round(self.degree + 273.15, 2)

    class Fahrenheit(Temperature):
        def __init__(self, degree):
            super().__init__(degree)
            self.name = 'F'

        def to_kelvin(self):
            return round((self.degree - 32) * (5 / 9) + 273.15, 2)

        def to_celsius(self):
            return round((self.degree - 32) * (5 / 9), 2)

    class Kelvin(Temperature):
        def __init__(self, degree):
            super().__init__(degree)
            self.name = 'K'

        def to_celsius(self):
            return round(self.degree - 273.15, 1)

        def to_fahrenheit(self):
            return round((self.degree - 273.15) * (9 / 5) + 32, 1)

    kelvin = Kelvin(21)
    celsius = Celsius(21)
    fahrenheit = Fahrenheit(21)

    print(f'{kelvin.degree} {kelvin.name} in Celsius: {kelvin.to_celsius()}')
    print(f'{kelvin.degree} {kelvin.name} in Fahrenheit: {kelvin.to_fahrenheit()}')

    print(f'{celsius.degree} {celsius.name} in Fahrenheit: {celsius.to_fahrenheit()}')
    print(f'{celsius.degree} {celsius.name} in Kelvin: {celsius.to_kelvin()}')

    print(f'{fahrenheit.degree} {fahrenheit.name} in Celsius: {fahrenheit.to_celsius()}')
    print(f'{fahrenheit.degree} {fahrenheit.name} in Kelvin: {fahrenheit.to_kelvin()}')


@header('2: In The Quantum Realm')
def make_exercise_2():
    from random import randint, random, choice

    def set_position():
        return randint(0, 10_000)

    def set_momentum():
        return random()

    def set_spin():
        return choice(['1/2', '-1/2'])

    class QuantumParticle:
        __position = None
        __momentum = None
        __spin = None

        def __init__(self):
            self.__position = set_position()
            self.__momentum = set_momentum()
            self.__spin = set_spin()

        def __repr__(self):
            return f'Quantum Particle info:\n\t' \
                   f'Position: {self.__position}\n\t' \
                   f'Momentum: {self.__momentum}\n\t' \
                   f'Spin: {self.__spin}\n'

        def disturbance(self):
            self.__position = set_position()
            self.__momentum = set_momentum()

        def get_position(self):
            self.disturbance()
            return self.__position

        def get_momentum(self):
            self.disturbance()
            return self.__momentum

        def get_spin(self):
            return self.__spin

        def entangle(self, other):
            if self.__spin == other.__spin:
                other.__spin = '1/2' if other.__spin == '-1/2' else '-1/2'
                print('Particle p1 is now in quantum entanglement with Particle p2')
            else:
                print('Spooky Action at a Distance')

    quant = QuantumParticle()
    quant2 = QuantumParticle()
    print(quant)
    print(quant2)
    quant.entangle(quant2)
    quant.entangle(quant2)


main()
