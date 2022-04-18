from random import shuffle 

userInput = input('Enter the string. (Your string must be exactly 10 characters): ')
length = len(userInput)

if (length == 10):
    
    print(f'\nFirst character: {userInput[0]}\nLast character: {userInput[length-1]}\n')
    oneByOne = ''
    
    for x in userInput:
        oneByOne += x
        print(oneByOne)

    listToShuffle = list(userInput)
    shuffle(listToShuffle)
    result = ''.join(listToShuffle)
    print(f'\n{result}\n')

elif (length > 10):
    print('You entered more than 10 chars.')

else:
    print('You entered less than 10 chars.')