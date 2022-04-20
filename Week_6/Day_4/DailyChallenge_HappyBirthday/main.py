import datetime

currentDate = datetime.datetime.now()
currentYear = int(currentDate.strftime('%Y'))

userInput = input('Enter your birthdate (DD/MM/YYYY): ')
userInput = userInput.split('/')
userDate = datetime.datetime(int(userInput[2]), int(userInput[1]), int(userInput[0]))
userAge = int(userDate.strftime('%Y'))

candles = 'i' * ((currentYear - userAge) % 10)
happy = ':'.join(list(' happy ')).strip()
birthday = ":".join(list(' birthday ')).strip()
arrows = '^' * len(birthday)
footer = "~" * (len(birthday) + 2)
x = '_' * int(((len(happy) - len(candles))/2))
spaces = ' ' * (int(((len(footer) - len(happy)) / 2)) - 2)

leapYear = userAge % 4 == 0 and userAge % 100 != 0 or userAge % 400 == 0
count = 2 if leapYear else 1

for _ in range(count):
    print(f' {spaces} {x}{candles}{x} {spaces}')
    print(f' {spaces}|{happy}|{spaces}')
    print(f' {"_"*len(spaces)}|{"_"*len(happy)}|{"_"*len(spaces)}')
    print(f'|{arrows}|')
    print(f'|{birthday}|')
    print(f'|{" " * len(birthday)}|')
    print(f'{footer}')