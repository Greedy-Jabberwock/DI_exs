from math import sqrt

def print_header(exercise_number):
    border = '-------------------------------'
    print(f'{border}\nExercise {exercise_number}:')


def make_exercise_1(element, pos, some_list):
    print('Insert function:')
    if pos > len(some_list):
        print('Sorry, out of range.')
    else:
        print(some_list)
        first_part = some_list[:pos]
        second_part = some_list[pos:]
        first_part.append(element)
        result = first_part+second_part
        print(result)
        return result


def make_exercise_2(given_string):
    print('Function to count spaces in given string:')
    print(f'Given string: "{given_string}"')
    spaces = given_string.count(' ')
    print(f'Spaces in string: {spaces}')
    return spaces


def make_exercise_3(given_string):
    print('Function counting uppercase and lowercase letters:')
    uppers = 0
    lowers = 0
    for letter in given_string:
        if letter.islower():
            lowers += 1
        elif letter.isupper():
            uppers += 1
    print(f'Given string: {given_string}')
    print(f'Count uppercase: {uppers}\nCount lowercase: {lowers}')


def make_exercise_4(nums_list):
    print("Function to sum all numbers in list")
    print(f'Given list: {nums_list}')
    total = 0
    for x in nums_list:
        total += x
    print(f'Sum of all elements: {total}')
    return total


def make_exercise_5(nums_list):
    print('Function to find max value:')
    print(f'Given nums: {nums_list}')
    maximum = -1_000_000
    for x in nums_list:
        maximum = x if maximum < x else maximum
    print(f'Max value is: {maximum}')
    return maximum


def make_exercise_6(number):
    print('Function calculates factorial of value:')
    print(f'Given number: {number}')
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f'Factorial of number is: {factorial}')
    return factorial


def make_exercise_7(given_list, char_to_count):
    print('Function counts an element in the given list:')
    print(f'Given list: {given_list}')
    counter = 0
    for letter in given_list:
        if letter == char_to_count:
            counter += 1
    print(f'In given list there a {counter} "{char_to_count}"')
    return counter


def make_exercise_8(num_list):
    print('L2-norm function:')
    print(f'Given nums: {num_list}')
    total = 0
    for x in num_list:
        total += round(sqrt(x))
    print(f'L2-norm result: {total}')
    return total


def make_exercise_9(given_list):
    print("Function to check monotonic:")
    print(f'Given list: {given_list}')
    order = 'asc' if given_list[0] < given_list[1] else 'dsc'
    mono = True
    for i in range(len(given_list)-1):
        if order == 'asc':
            if given_list[i] > given_list[i+1]:
                mono = False
                break
        else:
            if given_list[i] < given_list[i+1]:
                mono = False
                break
    print(f'Is mono? {mono}')
    return mono


def make_exercise_10(string_list):
    print('Function to find longest word:')
    print(f'Given list: {string_list}')
    longest = ''
    for i in string_list:
        if len(longest) < len(i):
            longest = i
    print(f'Longest word is "{longest}"')


def make_exercise_11(given_list):
    print("Function sort string and number values to two different lists.")
    print(f'Given list: {given_list}')
    str_list = []
    num_list = []
    for item in given_list:
        try:
            num_list.append(int(item))
        except ValueError:
            str_list.append(item)
    print(f"Strings: {str_list}")
    print(f'Numbers: {num_list}')
    return str_list, num_list


def make_exercise_12(some_string):
    print('Function to check is value a palindrome or not:')
    print(f'Given string: "{some_string}"')
    some_string = some_string.lower()
    checking_string = some_string[::-1]
    result = some_string == checking_string
    print(f'Is palindrome? {result}')
    return result


def make_exercise_13(string, value):
    print(f'Function to return amount of words in a '
          f'sentence with length > {value}:')
    print(f'Given string: "{string}"')
    words_to_check = string.split(' ')
    counter = 0
    for word in words_to_check:
        if len(word) > value:
            counter += 1
    print(f'There are {counter} words with length > {value}')
    return counter


def make_exercise_14(given_dict):
    print("Function that returns the average value in a dictionary:")
    print(f'Given dictionary: {given_dict}')
    total = 0
    for value in given_dict.values():
        total += value
    total /= len(given_dict.values())
    print(f'Average value: {round(total)}')
    return round(total, 2)


def make_exercise_15(num_1, num_2):
    print('Function that returns common divisors of 2 numbers:')
    print(f'Given numbers: {num_1}, {num_2}')
    divisors = []
    for x in range(2,num_2 + 1):
        if not num_1 % x and not num_2 % x:
            divisors.append(x)
    print(f'Common divisors: {divisors}')
    return divisors


def make_exercise_16(num):
    print('Function that test if a number is prime:')
    print(f'Given number: {num}')
    count_divs = False
    for x in range(2, num+1):
        if count_divs:
            break
        if not num % x:
            count_divs = True
    else:
        print('Number is prime.')
        return True
    print("Number is not prime.")
    return False


def make_exercise_17(test):
    print("unction that prints elements of a list if the index and the value are even:")
    print(f'Given list: {test}')
    result_list = []
    for index, value in enumerate(test):
        if not index % 2 and not value % 2:
            result_list.append(value)
    print(f'Result: {result_list}')


def make_exercise_18(**kwargs):
    print('Function that accepts an undefined number of keyworded arguments and return the count of different types:')
    print(f'Given arguments: {kwargs}')
    arguments = kwargs
    types = {}
    for value in arguments.values():
        el_type = str(type(value)).replace("<class '", '').replace("'>", '')
        if el_type in types:
            types[el_type] += 1
        else:
            types[el_type] = 1
    result_str = []
    for key, value in types.items():
        result_str.append(f'{key}: {value}')
    print('Result is:\n', ", ".join(result_str))
    return types


def make_exercise_19(some_str, separator = ' '):
    print('Function that mimics the builtin .split().')
    print(f'Given string: {some_str}')
    some_str += separator
    words = []
    word = ''
    for index, ch in enumerate(some_str):
        if ch == separator:
            words.append(word)
            word = ''
        else:
            word += ch
    print(f'Result: {words}')
    return words


def make_exercise_20(some_pass):
    print('Function converts a string into password format.')
    print(f'Given password: "{some_pass}"')
    hidden = '*' * len(some_pass)
    print(f'Hidden password: "{hidden}"')
    return hidden


def main():
    test = [f"Item{x}" for x in range(10)]

    print_header(1)
    test_insert = make_exercise_1('Inserted', 4, test)

    print_header(2)
    test = 'Alice in Wonderland     '
    test_spaces = make_exercise_2(test)

    print_header(3)
    test = 'SomE STRing wiTh RandOM cAsE'
    make_exercise_3(test)

    print_header(4)
    test = [1, 2, 35, 6, -9, -3, 25]
    test_sum = make_exercise_4(test)

    print_header(5)
    test = [1, 4, 6, 1, 5, 6, -88, 9]
    max_test = make_exercise_5(test)

    print_header(6)
    test = 10
    factorial = make_exercise_6(test)

    print_header(7)
    test = ['a', 'a', 't', 'o', 'x', 'z', 'a']
    count_test = make_exercise_7(test, 'a')

    print_header(8)
    test = [1, 2, 2]
    l2_norm_test = make_exercise_8(test)

    print_header(9)
    test = [2, 6, 5, 5, 2, 0]
    make_exercise_9(test)
    test = [2, 3, 3, 3]
    make_exercise_9(test)
    test = [1, 2, 8, 5]
    make_exercise_9(test)

    print_header(10)
    test = ['a', 'bsasaga', 'cannibalism']
    make_exercise_10(test)

    print_header(11)
    test = ['a', 1, 'bsasaga', 'cannibalism', 4, 'fsf', 6]
    sorted_values = make_exercise_11(test)

    print_header(12)
    test = 'Madam'
    is_palindrome = make_exercise_12(test)
    test = 'Crocodile'
    is_palindrome = make_exercise_12(test)

    print_header(13)
    test = 'Here we are or not here we are want to greet'
    test_n = 3
    sum_over_n = make_exercise_13(test, test_n)

    print_header(14)
    test = {'a': 1, 'b': 2, 'c': 8, 'd': 1}
    average = make_exercise_14(test)

    print_header(15)
    divisors = make_exercise_15(10, 20)

    print_header(16)
    test = 11
    make_exercise_16(test)

    print_header(17)
    test = [1, 2, 2, 3, 4, 5]
    make_exercise_17(test)

    print_header(18)
    diffr_types = make_exercise_18(a=1,b='string',c=1.0,d=True,e=False,
                                   f=True, g='False', h=-3)

    print_header(19)
    test = 'Alice in wonderland'
    splitted_str = make_exercise_19(test)

    print_header(20)
    password = input('Enter password to hide: ')
    hidden = make_exercise_20(password)


main()
