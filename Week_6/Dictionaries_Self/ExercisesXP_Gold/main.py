import random


border = '=========================='

# =========================EXERCISE 1-3: Birthday Look-Up=========================

print(f'{border}\nEXERCISE 1-3: Birthday Look-Up\n')

birthdays = {
    "Larry": '1995/03/22',
    "Ginger": '1984/12/01',
    "Sun Zhi": '2000/01/01',
    "Jacob": '1990/10/23',
    "William": '2012/06/13'
    }

print('Hello! I can help you to remember your friend\'s birthdays or yours!')
while True:
    print('\nAt now I know birthday dates of these people:\n'
          f'{", ".join(birthdays.keys())}\n'
          'If you don\'t need my help, input "exit".')
    userAnswer = input('Do you want to add a new person? (Y/N)\n')

    if userAnswer == 'Y':
        newName = input('Not a problem. Who must be added? Name must be unique.\n')
        if newName  in birthdays.keys():
            print('Sorry, but this name is already in the base.')
        else:
            newDate = input("And give me one's birthday date (YYYY/MM/DD)\n")
            birthdays[newName] = newDate

    if userAnswer == 'N':
        nameToFind = input('Give me some name, please.\n')
        print("Let's see...")
        if nameToFind in birthdays.keys():
            print('Yap, there it is!')
            edge = '----------------------------------------'
            personBirthday = birthdays[nameToFind]
            spaces = ' ' * int(((len(edge) - len(personBirthday)) / 2))
            print(f'\n {edge}\n'
                f'|{spaces}{personBirthday}{spaces}|\n'
                f' {edge}\n')
        else: 
            print('Sorry, I have no idea who is {}.\n'.format(nameToFind))
    
    if userAnswer == 'exit':
        print('Goodbye then!')
        break

print(f'\n{border}')

# =========================EXERCISE 4: Fruit Shop================================

print(f'EXERCISE 4: Fruit Shop\n')

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

sentence = 'Welcome to the store. Now we have: | '

for k, v in items.items():
    sentence += f'{v} {k}s | '

print(sentence)

for k, v in items.items():
    items[k] = (v, (random.randint(1, 7)/2))

total = 0
for x in items.values():
    total += x[0] * x[1]

print(items)
print(f'You need {total}$ to buy everything in the store.')

print(f'\n{border}')

# =========================EXERCISE 5 : Cars================================

print(f'EXERCISE 5 : Cars\n')

carsStr = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Fiat"
carsList = carsStr.split(', ')

print(f'There are {len(carsList)} companies in the list.\n')
carsList.sort()
carsList.reverse()
print(f'List in descending order:\n{carsList}')
oNames = 0
withoutINames = 0

for car in carsList:
    if 'o' in car: 
        oNames+=1
    if 'i' not in car:
        withoutINames += 1

print(f'\nHow many companies has the letter "o" in them: {oNames}')
print(f'\nHow many companies don\'t have the letter "i" in them: {withoutINames}')

# --------BONUS PART-----------

carsDupl = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
carsSet = set(carsDupl)
print(f'\nThere are {len(carsSet)} unique companies in list:\n{", ".join(carsSet)}')

carsList.reverse()
for i, car in enumerate(carsList):
    carsList[i] = car[::-1]

print(f'\n{", ".join(carsList)}')

print(f'\n{border}')
