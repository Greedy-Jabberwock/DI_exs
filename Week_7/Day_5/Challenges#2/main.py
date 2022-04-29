border = '--------------------------------------'

# =========================== Exercise 1 ================================

print(border)
print('Exercise 1')

stars = '*'

print()
for x in range(1,4):
    spaces = (3 - x) * ' '
    print(f'{spaces}{stars}{spaces}')
    stars += '*' * 2
print()

print()
for x in range(1,6):
    stars = '*' * x
    spaces = ' ' * (5 - len(stars))
    print(f'{spaces}{stars}')
print()

print()
lines = []
for x in range(1,6):
    stars = '*' * x
    spaces = ' ' * (5 - len(stars))
    line = f'{stars}{spaces}'
    lines.append(line)

lines_second = lines.copy()
lines_second.reverse()
for line in lines_second:
    line = line[::-1]
    lines.append(line)

for line in lines:
    print(line)
print()
print(border)

# =========================== Exercise 1 ================================

print(border)
print('Exercise 2')
# It's the bubble sort, I think.
my_list = [2, 24, 12, 354, 233]                                                    # Create list of integers
for i in range(len(my_list) - 1):                                                  # Loop through the all list elements
    minimum = i                                                                    # Flag element to check value
    for j in range(i + 1, len(my_list)):                                           # Nested loop to compare rest values of list
        if my_list[j] < my_list[minimum]:                                          # If current element lower then element to check ->
            minimum = j                                                            # -> reassign minimum value, to swap values
            if minimum != i:                                                       # i1: if element are equal swapping has no sense
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]        # i1: swap elements to sort list
print(my_list)

print(border)