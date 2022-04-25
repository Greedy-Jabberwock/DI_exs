from random import randint

border = '------------------------------'

# ----------------- Exercise 1 : What Are You Learning ? ---------------

print(border)
print('Exercise 1 : What Are You Learning ? ')


def display_message():
    print('I am learning Python right now!')


display_message()
print(border)

# ----------------- Exercise 2: What’s Your Favorite Book ? ------------

print(border)
print('Exercise 2: What’s Your Favorite Book ?')


def favorite_book(title):
    print(f'One of my favorite book is "{title}".')


favorite_book('Steel Rat')
print(border)

# ----------------- Exercise 3 : Some Geography ------------------------

print(border)
print('Exercise 3 : Some Geography')


def describe_city(city_name, country='Denmark'):
    print(f'{city_name.title()} is in {country.title()}.')


describe_city('Copenhagen')
print(border)

# ----------------- Exercise 4 : Random --------------------------------

print(border)
print('Exercise 4 : Random')


def compare_numbers(num1, num2=randint(1,100)):
    result_string = 'Success' if num1 == num2 else 'Fail'
    print(f'{num1} == {num2}\n{result_string}')


compare_numbers(23)
print(border)

# -------- Exercise 5 : Let’s Create Some Personalized Shirts ! --------

print(border)
print('Exercise 5 : Let’s Create Some Personalized Shirts !')


def make_shirt(message, size='large'):
    print(f'\nSize of the shirt: {size}\n'
          f'Message on the shirt: {message}')


s_message = 'I code, you code.'
make_shirt(message=s_message)
make_shirt(size='medium', message=s_message)
make_shirt(message=s_message, size='any')
print(border)

# ------------------ Exercise 6 : Magicians … --------------------------

print(border)
print('Exercise 6 : Magicians …')

magicians = ['Merlin', 'Reisline', 'Lokhart']


def show_magicians(mages):
    for name in mages:
        print(name)


def make_great(mages):
    for index, name in enumerate(mages):
        mages[index] = name + ' the Great'
    return mages


show_magicians(make_great(magicians))
