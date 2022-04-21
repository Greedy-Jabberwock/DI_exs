border = '-------------------------------------------------------------------'
userMessage = '''Some text for test.'''
userShift = 3
cypher_text = ''
uncypher_text = ''

while True:
    print(border)
    print('Hello! You can cypher or decipher your message. What do you want to do?')
    print('1 - cypher.\n2 - decipher.\nE - exit')
    print(border)
    userChoice = input()
    if userChoice == '1' or userChoice == '2' or userChoice == 'E':
        if userChoice == '1':
            userMessage = input('Enter your message to encrypt:\n')
            userShift = int(input('How many symbols do I need to shift?\n'))
            for letter in userMessage:
                cypher_text += chr(ord(letter) + userShift)
            print(border)
            print(f'Your cypher message:\n{cypher_text}')
            print(border)

        elif userChoice == '2':
            if cypher_text == '':
                print(border)
                print('Nothing to decipher.')
                print(border)
            else:
                for letter in cypher_text:
                    uncypher_text += chr(ord(letter) - userShift)

                print(border)
                print(f'Your original message:\n{uncypher_text}')
                print(border)
        else:
            break
    else:
        print(border)
        print('Invalid. Input 1 or 2')
        print(border)
        continue
