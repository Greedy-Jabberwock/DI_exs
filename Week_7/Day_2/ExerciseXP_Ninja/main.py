border = '------------------------------------'

# -------------------- Exercise 1 : Box Of Stars -----------------------

print(border)
print('Exercise 1 : Box Of Stars')

sentence = input('Input the sentence:\n').split(' ')


def box_printer(words_array):
    longest_word = find_longest_word(words_array)
    edge_line = '*' * len(longest_word)
    words_array.append(edge_line)
    words_array.insert(0, edge_line)
    for word in words_array:
        print_line(word, len(longest_word))


def find_longest_word(words):
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def print_line(word, max_length):
    if word[0] != '*':
        edge_str = '* '
    else:
        edge_str = '**'
    spaces = ' ' * (max_length - len(word))
    print(f'{edge_str}{word}{spaces}{edge_str[::-1]}')


box_printer(sentence)
print(border)

# --------------------Exercise 2 ---------------------------------------

print(border)
print('Exercise 2')

# This function swapping the elements to sort in ascending order


def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)

print(border)
