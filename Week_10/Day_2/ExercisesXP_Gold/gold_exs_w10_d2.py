import re
import string
from random import choice, randint

from helper import header


def return_numbers(text: str):
    return ''.join(re.findall(r'\d', text))


def check_name():
    # full_name = input('Enter your full name.\n>>>\t').strip()
    full_name = 'Jack Russel'
    pattern = r'^[A-Z]{1}[a-z]+\s{1}[A-Z]{1}[a-z]+$'
    return False if re.match(pattern, full_name) is None else True


def get_length():
    while True:
        try:
            user_length = int(input('Give me the length of password (6-30):\n>>>\t'))
            if 6 <= user_length <= 30:
                return user_length
            else:
                raise ValueError
        except ValueError:
            print('You should give me a number from 6 to 30.')
            continue


def generate_password(length):
    symbols = {
        'digit': {
            'symbols': string.digits,
            'priority': 0},
        'upper': {
            'symbols': string.ascii_uppercase,
            'priority': 0},
        'lower': {
            'symbols': string.ascii_lowercase,
            'priority': 0},
        'special': {
            'symbols': string.punctuation,
            'priority': 0}
    }
    password = ''
    types = tuple(symbols.keys())
    for i in range(length):
        symbol_type = choice(types)
        if i == 0:
            password += choice(symbols[symbol_type]['symbols'])
            symbols[symbol_type]['priority'] += 1
        else:
            if symbols[symbol_type]['priority'] >= i:
                i -= 1
                continue
            else:
                password += choice(symbols[symbol_type]['symbols'])
                symbols[symbol_type]['priority'] += 1
    return password


def test():
    print('''---------------------------------------------
        \rRequirements to passwords: 
        \rAt least 1 digit (0-9)
        \rAt least 1 lower-case character (a-z)
        \rAt least 1 upper-case character (A-Z)
        \rAt least 1 special character (eg. !, @, #, $, %, ^, _, …)
        \rOnce there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.
        \r---------------------------------------------''')
    passwords = (generate_password(randint(6, 30)) for _ in range(100))
    print()
    for password in passwords:
        digit_cond = re.findall(r'\d', password)
        lower_cond = re.findall(r'[a-z]', password)
        upper_cond = re.findall(r'[A-Z]', password)
        punct_cond = re.findall(r'\W', password)
        if upper_cond and lower_cond and digit_cond and punct_cond:
            print(f'{password}: Requirements are fulfilled.')
        else:
            print(f'{password}: Requirements are not fulfilled.')
    print()



def make_exercise3():
    test()
    length = get_length()
    password = generate_password(length)
    print(password)


def main():
    header('Exercise 1: Regular Expression #1')
    print(return_numbers('k5k3q2g5z6x9bn'))
    header('Exercise 2: Regular Expression #2')
    print('Is valid? ' + str(check_name()))
    header('Exercise 3: Python Password Generator')
    make_exercise3()


main()
