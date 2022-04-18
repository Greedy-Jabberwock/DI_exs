#=============================Exercise 1: Hello World===================================

print('================Exercise 1================\n')
hello = 'Hello World\n'
print(hello * 4)
print('==========================================\n')

#=============================Exercise 2 : Some Math====================================

print('================Exercise 2================\n')
power = (99^3) * 8
print(power)
print('\n==========================================\n')


#=============================Exercise 3 : What Is The Output ?=========================

print('================Exercise 3================\n')

print("5 < 3 ----------------- false")
print("3 == 3  --------------- true")
print("3 == '3' -------------- false")
print("'3' > 3 --------------- true. (Right answer: TypeError)")
print("'Hello' == 'hello' ---- false")

print('\n==========================================\n')

#=============================Exercise 4 : Your Computer Brand==========================

print('================Exercise 4================\n')

brand = 'Asus'
print(f'I have a {brand} computer')

print('\n==========================================\n')

#=============================Exercise 5 : Your Information=============================

print('================Exercise 5================\n')

name = 'Vitalii'
age = 28
shoe_size = 42
info = 'My name is {}, i\'m {} years old. My shoe size is {}.'.format(name, age, shoe_size)
print(info)

print('\n==========================================\n')

#=============================Exercise 6 : A & B========================================

print('================Exercise 6================\n')

a = 9
b = 15

if (a > b):
    print('Hello world.')
else: 
    print('b lesser then a')

print('\n==========================================\n')

#=============================Exercise 7 : Odd Or Even==================================

print('================Exercise 7================\n')

userNumber = int(input('Enter the number: '))

if (userNumber % 2 == 0): 
    print(f'{userNumber} is even')
else:
    print(f'{userNumber} is odd')

print('\n==========================================\n')

#=============================Exercise 8 : What’s Your Name ?===========================

print('================Exercise 8================\n')

userName = input('Enter your name:').lower()
myName = 'vitalii'
if (userName == myName):
    print('Wow, tattoo brothers!')


print('\n==========================================\n')

#=============================Exercise 9 : Tall Enough To Ride A Roller Coast===========

print('================Exercise 9================\n')

userHeigth = int(input('Enter your height(in inches): '))

if (userHeigth > 145):
    print('OK. You\'re tall enought to ride.')
else:
    print('Sorry, you must be bigger then 145 inches to ride a roller coaster.')

print('\n==========================================\n')
