import datetime

border = '--------------------------------------'

# -----------------Exercise 7: When Will I Retire ?---------------------


def get_birth_date():
    while True:
        try:
            year, month, day = input('Enter you date of birth, separated '
                                     'by "/"\n').strip().split('/')
            year = int(year)
            month = int(month)
            day = int(day)

            if 0 > month > 12 or 0 > day > 31 or 0 > year:
                raise TypeError
            return datetime.datetime(year, month, day)
        except (TypeError, ValueError):
            print('Invalid input. Try again')
            continue


def get_gender():
    gender = input('Enter your gender ("m" or "f"):\n')
    if gender in ('f', 'm'):
        return gender
    return get_gender()


def get_age(birthdate):
    current_date = datetime.datetime.now()
    age = current_date.year - birthdate.year
    if current_date.month == birthdate.month:
        if current_date.day >= birthdate.day:
            age += 1
    elif current_date.month > birthdate.month:
        age += 1

    return age


def can_retire(sex, birth):
    if sex == "m":
        retire = birth >= 67
    else:
        retire = birth >= 62
    return retire


def main():
    age = get_age(get_birth_date())
    gender = get_gender()
    retire_or_not = can_retire(sex=gender, birth=age)
    print(f'Yes, you can retire. Your age is {age}.'
          if retire_or_not else
          f'No, you can\'t retire yet. Your age is {age}')


print(border)
print('Exercise 7: When Will I Retire ?')
main()
print(border)

# ---------------------------Exercise 8-------------------------------

print(border)
print('Exercise 8: ')


def get_integer():
    try:
        user = int(input('Give me some number: '))
        return user
    except TypeError:
        return get_integer()


def make_exercise(num):
    result_str = ''
    result = 0
    for i in range(1, num + 1):
        result_str += f'{str(num) * i} + ' if i < 4 else f'{str(num) * i}'
        result += int(str(num) * i)
    print(result_str, end=f' = {result}')


def secondary():
    make_exercise(get_integer())


secondary()