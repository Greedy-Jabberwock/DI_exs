# ===========================FizzBuzz Exercise===================================

userInput = int(input('Print a number between 1 and 100: '))
dividedBy5 = userInput % 5 == 0
dividedBy3 = userInput % 3 == 0
fizz = 'Fizz'
buzz = 'Buzz'

# if dividedBy5 and dividedBy3:
#     print(fizz, end=buzz)
# elif dividedBy5:
#     print(buzz)
# elif dividedBy3:
#     print(fizz)
# else:
#     print('Not divided by 5 or 3')

print('Fizz' if dividedBy3 else '', end='Buzz' if dividedBy5 else '\n');
