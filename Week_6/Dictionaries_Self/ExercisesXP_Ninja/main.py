from random import randint

border = '=========================='

# =========================EXERCISE : List Of Integers - Randoms=========================

print(f'{border}\nEXERCISE : List Of Integers - Randoms\n')

randNums = [randint(-100, 100) for _ in range(randint(50, 123))]

print(randNums)

print(f'\n{border}')

# =========================EXERCISE 2: Authentication CLI - Login=========================

print(f'{border}\nEXERCISE 2: Authentication CLI - Login\n')

users = {
    'valio325': 'speech1',
    'jeremiaFink': '12345a',
    'vLiZd': 'qwerty'
}
logged_in = []

marker = True

while marker:
    userInput = input('Do you want sign up, login or exit?\n')
    if userInput == 'exit':
        marker = False
    if userInput == 'login':
        username = input('Input your username.\n')
        if username in users.keys():
            password = input('Enter your password.\n')
            if password == users[username]:
                print('You are now logged in.')
                logged_in.append(username)
            else:
                print('Wrong password.')
        else:
            print('There is no such user. You need to sign up.')
    if userInput == 'sign up':
        while True:
            username = input('Create your username.\n')
            if username not in users.keys():
                password = input('Create your password.\n')
                users[username] = password
                break
            else:
                print('Sorry, this username is invalid.')

print(f'\n{border}')