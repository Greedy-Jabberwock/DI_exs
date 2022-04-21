import random

border = '=========================='

# =========================EXERCISE 1 : Concatenate Lists=======================

print(f'{border}\nEXERCISE 1 : Concatenate Lists\n')

list1 = [1, 3, 5.2, True]
list2 = ['s', False, {'id': 1}]
list1.extend(list2)
print(list1)

print(f'\n{border}')

# =========================EXERCISE 2: Greatest Number====================================

print(f'EXERCISE 2: Greatest Number\n')

greatest = 0

for index, item in enumerate(range(3)):
    currentI = index+1
    suffix = 'st'
    if currentI == 2:
        suffix = 'nd'
    if currentI == 3:
        suffix = 'rd'
    userNumber = int(input(f'Input the {currentI}{suffix} number: '))
    if greatest < userNumber:
        greatest = userNumber

print(f'\nThe greatest number is: {greatest}')

print(f'\n{border}')

# =========================EXERCISE 3 : The Alphabet================

print(f'EXERCISE 3 : The Alphabet\n')

aIndex = 97
vowels = 'aeiou'

for _ in range(26):
    character = chr(aIndex)
    print(f'{character} is a {"vowel" if character in vowels else "consonant"}')
    aIndex += 1

print(f'\n{border}')

# =========================EXERCISE 4==================================

print(f'EXERCISE 4\n')

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

userName = input('Enter the name:\n')

if userName in names:
    print(f'First occurence: {names.index(userName)}.')
else:
    print("There is no such name in the list.")

print(f'\n{border}')

# =========================EXERCISE 5 : Words And Letters===========================

print(f'EXERCISE 5 : Words And Letters\n')

words = []

for _ in range(7):
    words.append(input('Enter the word:\n').lower())

letter = input('\nNow enter the letter:\n').lower()
print()

for i in words:
    if letter in i:
        print(f'Index "{letter}" in "{i}": {i.index(letter)}')
    else:
        print(f'Unfortunately, there is no "{letter}" in "{i}"')

print(f'\n{border}')

# =========================EXERCISE 6 : Loop===================================

print(f'EXERCISE 6 : Loop\n')

million = [x + 1 for x in range(1000000)]
print(f'Minimal value: {min(million)}\n'
      f'Maximum value: {max(million)}')

total = sum(million)

print(f'Sum of million values is {total}')

print(f'\n{border}')

# =========================EXERCISE 7==========================================

print(f'EXERCISE 7\n')

userNums = input('Enter the numbers, separated by comma: ').split(',')
print(userNums)
userNums = tuple(userNums)
print(userNums)

print(f'\n{border}')

# =========================EXERCISE 8 : Random Number==========================================

print(f'EXERCISE 8 : Random Number\n')

userNum = ''
randomNum = random.randint(1, 9)
countWin = 0
countLoss = 0

while True:

    while True:
        userNum = input('Input a number from 1 to 9: ')
        if userNum.isdigit():
            userNum = int(userNum)
            if 1 <= userNum <= 9:
                break
        elif userNum == 'exit':
            break

    if userNum == 'exit':
        break
    elif userNum == randomNum:
        print('\nWinner!')
        countWin += 1
        randomNum = random.randint(1, 9)
    else:
        print('\nLose!')
        countLoss += 1

    print('\n----------- '
          f'Wins: {countWin} -- '
          f'Loses: {countLoss} -- '
          f'For exit input "exit" '
          '----------\n')

print(f'\n{border}')

