

# ================== Exercise 1: What's Your Name ==================


def get_full_name(f_name, l_name, m_name=''):
    if m_name == '':
        m_name = ' '
    else:
        m_name = f' {m_name.title()} '
    print(f'{f_name.title()}{m_name}{l_name.title()}')


def make_exercise_1():
    get_full_name('bruce', 'Lee')
    get_full_name(l_name='Clinton', f_name='Bill')
    get_full_name('John', 'Lee', 'Hooker')


def make_exercise_2():
    morse = {
        'a': '._',
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': ".",
        'f': ".._.",
        'g': "__.",
        'h': "....",
        'i': "..",
        'j': ".___",
        'k': "_._",
        'l': "._..",
        'm': "__",
        'n': "_.",
        'o': "___",
        'p': ".__.",
        'q': "__._",
        'r': "._.",
        's': "...",
        't': "_",
        'u': ".._",
        'v': "..._",
        'w': ".__",
        'x': "_.._",
        'y': "_.__",
        'z': "__..",
        '.': "._._._",
        ',': "__..__",
        '?': "..__..",
        '/': "-.._.",
        '@': "..._._",
        '1': ".____",
        '2': "..___",
        '3': "...__",
        '4': "...._",
        '5': ".....",
        '6': "_....",
        '7': "__...",
        '8': "___..",
        '9': "____.",
        '0': "_____",
    }
    result = ''
    sentence = input('Enter sentence to code in morse.\n').lower()
    for letter in sentence:
        if letter.isdigit() or letter.isalpha():
            result += f'{morse[letter]},'
        elif letter == ' ':
            result += '/'
        else:
            result += f'/{morse[letter]}/'
    print(result)


def main():
    border = '-------------------------------------'
    print(border)
    print('Exercise 1: What\'s Your Name')
    make_exercise_1()
    print(border)
    print('Exercise 2 : From English To Morse')
    make_exercise_2()
    print(f'\n{border}')


main()

