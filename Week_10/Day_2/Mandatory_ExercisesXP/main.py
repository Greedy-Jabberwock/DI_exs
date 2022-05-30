def header(exercise):
    print('\n==========================================\n'
          f'Exercise {exercise}\n'
          f'==========================================\n')


def make_exercise1():
    from func import add
    print(add(3, 6))


def make_exercise2():
    from random import randint

    def check_random_numbers(value):
        checker = randint(1, 100)
        if checker == value:
            print(f'{value} and {checker} are equal.')
        else:
            print(f'{value} and {checker} are not equal.')

    value_to_check = randint(1, 100)
    check_random_numbers(value_to_check)


def make_exercise3():
    import string
    from random import choices

    alpha = string.ascii_letters
    some_string = "".join(choices(alpha, k=5))
    print(some_string)


def make_exercise4():
    from datetime import datetime as d
    print(d.now().strftime('%d/%m/%Y'))


def make_exercise5():
    from datetime import datetime
    import time
    current_date = datetime.now()
    next_year = datetime(year=current_date.year+1, month=1, day=1)
    remain = next_year - current_date
    delta_as_time = time.gmtime(remain.total_seconds())
    print(f'Time until the New Year: {remain.days} days,'
          f'{time.strftime("%H:%M:%S", delta_as_time)} hours.')


def make_exercise6():
    from datetime import datetime
    birthday = datetime(1994, 10, 26)
    current_time = datetime.now()
    how_many_minutes = round((current_time - birthday).total_seconds() / 60)
    print(f'Your lifetime in minutes: {how_many_minutes}')


def make_exercise7():
    from datetime import datetime as dt
    import time
    day_of_children = dt(2022, 6, 1)
    current_time = dt.now()
    remain = day_of_children - current_time
    remain_as_time = time.gmtime(remain.total_seconds())
    print(f'Current date: {current_time.strftime("%D-%M-%M")}.\n'
          f'Next global holiday - Day of the Children.\n'
          f'Time remains until holiday: {remain.days} days, '
          f'{time.strftime("%H:%M:%S", remain_as_time)} hours.')


def make_exercise8():
    earth_year = 31_557_600  # in seconds
    calculate_alien_year = lambda x: x * earth_year
    mercury_year = calculate_alien_year(0.2408467)
    venus_year = calculate_alien_year(0.61519726)
    mars_year = calculate_alien_year(1.8808158)
    jupiter_year = calculate_alien_year(11.862615)
    saturn_year = calculate_alien_year(29.447498)
    uranus_year = calculate_alien_year(84.016846)
    neptune_year = calculate_alien_year(164.79132)
    calculate_age = lambda x, y: round(x / y, 2)
    test_age = 1_000_000_000
    all_values = {'Earth': calculate_age(test_age, earth_year),
                  'Mercury': calculate_age(test_age, mercury_year),
                  'Venus': calculate_age(test_age, venus_year),
                  'Mars': calculate_age(test_age, mars_year),
                  'Jupiter': calculate_age(test_age, jupiter_year),
                  'Saturn': calculate_age(test_age, saturn_year),
                  'Uranus': calculate_age(test_age, uranus_year),
                  'Neptune': calculate_age(test_age, neptune_year)}
    print(f'Your age: {test_age} seconds.')
    for key, value in all_values.items():
        print(f'You are {value} {key}-years old.')


def make_exercise9():
    from faker import Faker

    users = []

    def add_fake(code=None):
        user = Faker(code)
        user_info = {
            'name': user.name(),
            'address': user.address(),
            'language': 'EN' if code is None else code
        }
        users.append(user)
        print(user_info)

    add_fake('IT')
    add_fake()


def main():
    header('1: Import')
    make_exercise1()
    header('2: Random Module')
    make_exercise2()
    header('3: String Module')
    make_exercise3()
    header('4: Current Date')
    make_exercise4()
    header('5: Amount Of Time Left Until January 1st')
    make_exercise5()
    header('6 : Birthday And Minutes')
    make_exercise6()
    header('7 : Upcoming Holiday')
    make_exercise7()
    header('8 : How Old Are You On Jupiter?')
    make_exercise8()
    header('9 : Faker Module')
    make_exercise9()


main()
