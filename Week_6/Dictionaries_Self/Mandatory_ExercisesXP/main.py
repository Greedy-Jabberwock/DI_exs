from dis import dis


border = '=========================='

# =========================EXERCISE 1: Convert Lists Into Dictionaries=========================

print(f'{border}\nEXERCISE 1: Convert Lists Into Dictionaries\n')

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
zipper = zip(keys, values)

print(dict(zipper))

print(f'\n{border}')

# =========================EXERCISE 2: Cinemax#2================================

print(f'EXERCISE 2: Cinemax#2\n')

family_ticket = 0
family = {}

peopleCount = int(input('How many people in family?\n'))

for p in range(peopleCount):
    ticketCost = 0
    name = input('What is your name?\n')
    age = int(input('How old are you?\n'))
    if age <= 3:
        ticketCost = 0
        print('This ticket is free for you.')
    elif age <= 12:
        ticketCost = 10
        print('This ticket costs 10$')
        family_ticket += 10
    else:
        ticketCost = 15
        print('This ticket costs 15$')
        family_ticket += 15
    family[name] = ticketCost

print(f'\nFamily: {family}')
print(f'Your total price for family is {family_ticket}$. Enjoy your movie.\n')

print(f'\n{border}')

# =========================EXERCISE 3: Zara=========================

print(f'{border}\nEXERCISE 3: Zara\n')

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    "major_color": {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'red']
    }
}

brand['number_stores'] = 2

print(f'\n{brand["name"]} was founded in {brand["creation_date"]} for created'
      f'clothes for {brand["type_of_clothes"][:3]}')

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')
del brand['creation_date']

print(f'\nLast value of international competitors: '
      f'{brand["international_competitors"][-1]}')

print(f'\nMajor clother colors in the USA: {brand["major_color"]["US"]}')

print(f'\nAmount of key value pairs: {len(brand.items())}')

for key, value in brand.items():
    print(f'----------\nKey: {key}\nValue: {value}')

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10_000
}

brand.update(more_on_zara) # if key already is in the original dictionary
                           # this value will be reassigned. 
                           # If not - it will be created

print(f'\nStore numbers: {brand["number_stores"]}')

print(f'\n{border}')

# =========================EXERCISE 3: Disney Characters=========================

print(f'{border}\nEXERCISE 3: Disney Characters\n')

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
usersSorted = users.copy()
usersSorted.sort()

disney_users_A = {}
disney_users_B = {}
disney_users_C = {}

for i, x in enumerate(users):
    disney_users_A[x] = i
    disney_users_B[i] = x
    disney_users_C[usersSorted[i]] = i

print(f'{disney_users_A}\n')
print(f'{disney_users_B}\n')
print(f'{disney_users_C}\n')

containsI = filter(lambda x: True if 'i' in x.lower() else False, users)
starts_M_or_P = filter(lambda x: True if x.lower().startswith(('m','p')) else False, users)

print(f'\nContains "i": {", ".join(containsI)}')
print(f'\nStarts with "m" or "p": {", ".join(starts_M_or_P)}\n')

print(border)
