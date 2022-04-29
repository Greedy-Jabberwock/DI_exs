from random import choice

words_list = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
              'credit card', 'rush', 'south']
word = choice(words_list)
hangman = {
    'head': (' ', 'O'),
    'r_arm': (' ', '/'),
    'body': (' ', '|'),
    'l_arm': (' ', '\\'),
    'r_leg': (' ', '/'),
    'l_leg': (' ', '\\')
}
attempts = {
    'head': 1,
    'body': 1,
    'l_arm': 1,
    'r_arm': 1,
    'l_leg': 1,
    'r_leg': 1
}
already_guessed = set()


def print_gallows(hidden):
    head = hangman['head'][0] if attempts['head'] else hangman['head'][1]
    body = hangman['body'][0] if attempts['body'] else hangman['body'][1]
    l_arm = hangman['l_arm'][0] if attempts['l_arm'] else hangman['l_arm'][1]
    r_arm = hangman['r_arm'][0] if attempts['r_arm'] else hangman['r_arm'][1]
    l_leg = hangman['l_leg'][0] if attempts['l_leg'] else hangman['l_leg'][1]
    r_leg = hangman['r_leg'][0] if attempts['r_leg'] else hangman['r_leg'][1]

    print(f"""
    =================
    ||        |
    ||        {head}   
    ||       {r_arm}{body}{l_arm}
    ||       {r_leg} {l_leg}
    ||
    ||     {hidden}
    """)


def hide_word():
    hidden = ''
    for ch in word:
        if ch == ' ':
            hidden += ' '
        else:
            hidden += '_'
    return hidden


def get_valid_letter():
    not_valid = True
    while not_valid:
        letter = input('Give me a letter.\n').lower()
        if len(letter) != 1 or not letter.isalpha():
            print('Only one word and only letter.')
            continue
        elif letter in already_guessed:
            print('You already guessed tried this letter.')
            continue
        else:
            already_guessed.add(letter)
            return letter


def check_match(letter, hidden):
    hidden_list = [x for x in hidden]
    if letter in word:
        for index, ch in enumerate(word):
            if letter == word[index]:
                hidden_list[index] = letter
        hidden = ''.join(hidden_list)
        return hidden
    else:
        for key, value in attempts.items():
            if value == 1:
                attempts[key] = 0
                break
        print('Letter not in word')
        return hidden


def check_win(hidden_word):
    if hidden_word == word:
        print('You win')
        return False
    elif 1 not in attempts.values():
        print('You lose.')
        return False
    else:
        return True


def main():
    print('----------------------------------')
    print('Welcome to the "Hangman" game. Enjoy, and stay alive.')
    print('----------------------------------')
    print('Hiding the word...\nDone.')
    not_win = True
    hidden_word = hide_word()
    while not_win:
        print_gallows(hidden_word)
        user_letter = get_valid_letter()
        hidden_word = check_match(user_letter, hidden_word)
        not_win = check_win(hidden_word)
        if not not_win:
            print()
            print_gallows(hidden_word)


main()
