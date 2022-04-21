import math

border = '=========================='

# =========================EXERCISE 1 : Formula=======================

print(f'{border}\nEXERCISE 1 : Formula\n')

userNums = input('Enter three numbers, separated by comma: ').split(',')

for x in userNums:
    x.strip()
    x = int(x)

C = 50
H = 30
result = []

for x in userNums:
    q = int(math.sqrt((2 * C * int(x)) / H))
    result.append(str(q))

print(', '.join(result))

print(f'\n{border}')

# =========================EXERCISE 2: List Of Integers====================================

print(f'EXERCISE 2: List Of Integers\n')

nums = []
count = 0

while count < 10:
    userNum = input('Enter the number between -100 and 100: ')
    try:
        userNum = int(userNum)
        if -100 <= userNum <= 100:
            nums.append(userNum)
            count += 1
        else:
            print('Invalid number. Try again.')
            continue
    except TypeError:
        print('Not a number. Try again.')

print(f'\nList in one line: {nums}')
firstLast = [nums[0], nums[-1]]
nums.sort()
nums.reverse()
print(f'Sorted list: {nums}')

total = 0
greater50 = []
smaller10 = []
squared = []
largest = -101
smallest = 100

for x in nums:
    total += x
    if x > 50:
        greater50.append(x)
    if x < 10:
        smaller10.append(x)
    squared.append(x ** 2)
    if largest < x:
        largest = x
    if smallest > x:
        smallest = x


print(f'Sum of all numbers')
print(f'First and last items: {firstLast}')
print(f'All numbers greater than 50: {greater50}')
print(f'All numbers smaller than 10: {smaller10}')
print(f'All numbers squared: {squared}')
print(f'List without duplicates: {set(nums)}')
print(f'Average of all numbers: {round(total / len(nums), 2)}')
print(f'The largest number: {largest}')
print(f'The greatest number: {smallest}')

print(f'\n{border}')

# =========================EXERCISE 3 : Working On A Paragraph================

print(f'EXERCISE 3 : Working On A Paragraph\n')

paragraph = """Bubble sort works on the repeatedly swapping of adjacent elements until they are 
not in the intended order. It is called bubble sort because the movement of array elements is just 
like the movement of air bubbles in the water. Bubbles in water rise up to the surface; similarly, 
the array elements in bubble sort move to the end in each iteration."""

characters = len(paragraph)
sentences = paragraph.split('. ')
words = paragraph.split(' ')
nonSpace = 0
uniqueWords = []
nonUnique = 0
averageAmount = 0
wordsInSentence = 0

for i in paragraph:
    if i != ' ':
        nonSpace += 1

for s in sentences:
    wordsInSentence += len(s.split(' '))
averageAmount = wordsInSentence / len(sentences)

for w in words:
    if w not in uniqueWords:
        uniqueWords.append(w)
    else:
        nonUnique += 1

print('----------------------ANALYZING TEXT-----------------------')
print('-----------------------------------------------------------')
print(f'* Amount of characters: {characters}')
print(f'* Amount of sentences: {len(sentences)}')
print(f'* Amount of words: {len(words)}')
print(f'* Amount of unique words: {len(uniqueWords)}')
print(f'* Amount of whitespaces: {nonSpace}')
print(f'* Average amount of words per sentence: {round(averageAmount, 2)}')
print(f'* Amount of non-unique words in paragraph: {nonUnique}')
print('-----------------------------------------------------------')

print(f'\n{border}')

# =========================EXERCISE 4==================================

print(f'EXERCISE 4\n')

userSentence = input('Enter the sentence: ').split(' ')
sentenceSet = set(userSentence)
analyze = {}

for word in userSentence:
    analyze[word] = userSentence.count(word)

for key, value in analyze.items():
    print(f'{key}:{value}')

print(f'\n{border}')