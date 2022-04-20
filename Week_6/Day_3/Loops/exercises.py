border = '===================================='
#============================Exercise for loop==========================

print(border)

userNumber = int(input('Enter the number: ')) + 1

for x in range(1, userNumber):
    line = ''
    for y in range(1, userNumber):
        line += f'{x*y} '
    print(line)

print(border)

#============================Exercise while loop========================

print(border)

x = 1
while x < 11:
    print(x)
    x += 1

print(border)