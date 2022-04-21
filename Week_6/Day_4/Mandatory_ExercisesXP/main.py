border = '=========================='

# =========================EXERCISE 1: Favorite Numbers=========================

print(f'{border}\nEXERCISE 1: Favorite Numbers\n')

my_fav_numbers = {5, 13, 57}
my_fav_numbers.add(8)
my_fav_numbers.add(23)
my_fav_numbers.pop()

friend_fav_numbers = {33, 55, 13}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

print(f'\n{border}')

# =========================EXERCISE 2: Tuple====================================

print(f'EXERCISE 2: Tuple\n')

int_tuple = (1, 2, 4, 5)

# Tuple is immutable type of list, so you can't add new values to tuple, but you can create new tuple.
try:
    int_tuple.add(2)
except AttributeError:
    print("You cannot add new values to immutable type.")

print(f'\n{border}')

# =========================EXERCISE 3: Print A Range Of Numbers================

print(f'EXERCISE 3: Print A Range Of Numbers\n')

for n in range(1, 21):
    print(n)

print(f'\n{border}')

# =========================EXERCISE 4: Floats==================================

print(f'EXERCISE 4: Floats\n')

# Instead of integer, float is number with point.

# To create sequence of floats you can create int list,
# and then iterate it and divide each int by 1 or use 'str()' method.

x = 1
arr = []
while x < 5:
    x += 0.5
    if x % int(x) == 0:
        arr.append(int(x))
    else:
        arr.append(x)

print(arr)

print(f'\n{border}')

# =========================EXERCISE 5: Shopping List===========================

print(f'EXERCISE 5: Shopping List\n')

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(f'List at start:\n{basket}')
basket.remove('Banana')
basket.remove('Blueberries')
print(f'\nRemoving "Banana" and "Blueberries"\n{basket}')
basket.append('Kiwi')
print(f'\nAdding "Kiwi" to the end of the list\n{basket}')
basket.insert(0, 'Apples')
print(f'\nAdding "Apples to the beginning of the list"\n{basket}')
apples_count = basket.count('Apples')
print(f'\nApples in list: {apples_count}')
basket.clear()
print(f'\nClearing basket:\n{basket}')

print(f'\n{border}')

# =========================EXERCISE 6 : Loop===================================

print(f'EXERCISE 6 : Loop\n')

exitName = 'Vitalii'

while True:
    name = input('Enter your name: ')
    if name == exitName:
        break

print(f'\n{border}')

# =========================EXERCISE 7==========================================

print(f'EXERCISE 7\n')

arr = ['Hello', 'light', True, [1, 2, 3, 4], 2525, 'poorer', ('a', 'b')]

for index, item in enumerate(arr):
    if not index % 2:
        print(item)

print(f'\n{border}')

# =========================EXERCISE 8==========================================

print(f'EXERCISE 8\n')

for i in range(1500, 2501):
    if not i % 5 and not i % 7:
        print(i)

print(f'\n{border}')

# =========================EXERCISE 9: Favorite Fruits=========================

print(f'EXERCISE 9: Favorite Fruits\n')

fav_fruits = input('Enter you favorite fruits, separated by space: ').lower().split(' ')

userChoice = input("Enter the name of any fruit: ").lower()

if userChoice in fav_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')

print(f'\n{border}')

# =========================EXERCISE 10: Who Ordered A Pizza ?==================

print(f'EXERCISE 10: Who Ordered A Pizza ?\n')

toppings = []

while True:
    topping = input('Enter the topping to your pizza: ').lower()
    if topping == 'exit':
        break
    else:
        print(f'{topping.title()} added to your pizza.\n')
        toppings.append(topping)

price = 10 + len(toppings) * 2.5

print(f'\nYour toppings: {", ".join(toppings)}.\nYour order costs {price}$.'
      f'\nEnjoy your pizza!')

print(f'\n{border}')

# =========================EXERCISE 11: Cinemax================================

print(f'EXERCISE 11: Cinemax\n')

family_ticket = 0

peopleCount = int(input('How many people in family?\n'))

for p in range(peopleCount):
    age = int(input('How old are you?\n'))
    if age <= 3:
        print('This ticket is free for you.')
    elif age <= 12:
        print('This ticket costs 10$')
        family_ticket += 10
    else:
        print('This ticket costs 15$')
        family_ticket += 15

print(f'\nYour total price for family is {family_ticket}$. Enjoy your movie.\n')

teensCount = int(input('\nHow many teenagers want to watch the movie?\n'))
teensAllow = []

for t in range(teensCount):
    teenName = input('\nWhat is your name, young man?\n')
    teenAge = int(input('How old are you?\n'))
    if 16 < teenAge < 21:
        teensAllow.append({teenName: f'{teenAge} y.o.'})
        print("You allowed to watch th movie.\n")
    else:
        print('You are not allowed. Sorry, rules are rules.\n')

print('This teens can see the movie: ')
for x in teensAllow:
    for key, value in x.items():
        print(f'{key}, {value}')

print(f'\n{border}')

# =========================EXERCISE 12 : Who Is Under 16?======================

print(f'EXERCISE 12 : Who Is Under 16?\n')

names = ['John', 'Josh', 'Cristie', 'Crystal', 'Darron']
toRemove = []

print(f"Names before removing: {', '.join(names)}")

for person in names:
    age = int(input(f'How old are you, {person}?\n'))
    if age < 16:
        toRemove.append(person)

for x in toRemove:
    names.remove(x)

print(f"Names after removing: {', '.join(names)}")

print(f'\n{border}')

# =========================EXERCISE 13=========================================

print(f'EXERCISE 13\n')

sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'salat', 'pastrami', 'omelette']
finished_sandwiches = []

for s in sandwich_orders:
    finished_sandwiches.append(s)
    print(f'I made your {s} sandwich.')

sandwich_orders.clear()

print(f'\n{border}')

# =========================EXERCISE 14=========================================

print(f'EXERCISE 14\n')

print('Sorry, the restaurant is out of the pastrami.')

sandwich_orders13 = ['pastrami',
                     'tuna',
                     'pastrami',
                     'salat',
                     'pastrami',
                     'omelette',
                     'pastrami',
                     'cheese']
outOf = 'pastrami'

while outOf in sandwich_orders13:
    sandwich_orders13.remove(outOf)

print(f'Available sandwiches:\n{", ".join(sandwich_orders13)}')
