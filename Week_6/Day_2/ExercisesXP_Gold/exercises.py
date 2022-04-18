border = '================================\n'

#===================EXERCISE 1: Hello World-I Love Python=========================

print(border + 'Exercise 1: Hello World-I Love Python\n')

print('Hello World\n'*4 + 'I love Python\n'*4)

print(border)

#===================EXERCISE 2 : What Is The Season ?=========================

print(border + 'Exercise 2 : What Is The Season ?\n')

userChoice = int(input('Input a number of month (1-12): '))
season = ''
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if (userChoice in winter):
    season = 'winter'
elif (userChoice in spring):
    season = 'spring'
elif (userChoice in summer):
    season = 'summer'
elif (userChoice in autumn):
    season = 'autumn'

print(f'Season is: {season}')

print(border)
