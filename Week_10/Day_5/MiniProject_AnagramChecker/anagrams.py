from anagram_checker import AnagramChecker


def show_menu():
    print('''
    ---------------------------------------
    Hello! I can find anagrams to words. Do you want to try?
    c - continue
    e - exit
    ---------------------------------------''')


def get_choice():
    choice = input('>>> ')
    if choice == 'c':
        return 1
    elif choice == 'e':
        return None
    else:
        print('Only two options, sorry...')
        get_choice()


def get_word():
    user_word = input('Enter the word.\n>>> ').strip()
    return is_valid(user_word)


def is_valid(word):
    if word.isalpha():
        return word
    raise TypeError('Only one letters word is allowed.')


def get_anagrams(user_word):
    checker = AnagramChecker('sowpods.txt')
    return checker.get_anagrams(user_word)


def print_result(word, result):
    print(f'''----------------------------------
            \rYou give me the word "{word}"
            \rLet\'s see...''')
    if len(result) == 0:
        print('Sorry, I did not find any anagrams to your word.')
    else:
        print('I found this anagrams for your word: ')
        print(', '.join(result))
    print('----------------------------------')


def main():
    while True:
        show_menu()
        if get_choice() is None:
            print('Goodbye!')
            break
        user_word = get_word()
        anagrams = get_anagrams(user_word)
        print_result(user_word, anagrams)


if __name__ == '__main__':
    main()