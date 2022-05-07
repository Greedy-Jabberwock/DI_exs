from random import choice

# ====================== Rock, Paper, Scissors ==========================


def show_menu():
    print('(g) Play a new game')
    print('(x) Show scores and exit')


def continue_playing():
    choice = input('\t:\t')
    if len(choice) == 1:
        if choice == 'x':
            return False
        else:
            return True
    else:
        print('Invalid command.')
        return continue_playing()


def get_user_item():
    item = input('Select (r)ock, (p)aper or s(cissors):\t')
    if item in 'rps' and len(item) == 1:
        if item == 'r':
            return 'rock'
        elif item == 'p':
            return  'paper'
        elif item == 's':
            return 'scissors'
    else:
        print('Invalid input!')
        get_user_item()


def get_ai_choice(rules_dict):
    keys = list(rules_dict.keys())
    ai_choice = choice(keys)
    return ai_choice


def check_win(player, ai, rules, scores):
    result = ''
    if player == ai:
        result = 'draw'
        scores['draws'] += 1
    elif rules[player] == ai:
        result = 'lose'
        scores['loses'] += 1
    elif rules[ai] == player:
        result = 'win'
        scores['wins'] += 1
    print(f'You chose: {player}.\nComputer chose: {ai}.\nResult: {result}')


def print_scores(scores_dict):
    print('Game results:')
    print(f'\tYou won {scores_dict["wins"]} times.')
    print(f'\tYou lost {scores_dict["loses"]} times.')
    print(f'\tYou drew {scores_dict["draws"]} times.')


def game():
    rules = {'rock': 'paper',
             'paper': 'scissors',
             'scissors': 'rock'}
    scores = {'wins': 0,
              'loses': 0,
              'draws': 0}
    while True:
        show_menu()
        if continue_playing():
            user_item = get_user_item()
            ai_item = get_ai_choice(rules)
            check_win(user_item, ai_item, rules, scores)
        else:
            print_scores(scores)
            break
    # get_user_input
    # get_ai_choice
    # check_win
    # else: show_results


game()
