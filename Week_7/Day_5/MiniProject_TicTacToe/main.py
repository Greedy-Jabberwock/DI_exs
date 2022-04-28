from random import randint

border = '========================================'
empty_cell = '   '
cells = [
    [empty_cell, empty_cell, empty_cell],
    [empty_cell, empty_cell, empty_cell],
    [empty_cell, empty_cell, empty_cell]
]

players = {
    'first_player': {
        'sign': 'X',
        'human': False,
        'coordinates': {
            'x': None,
            'y': None
        }
    },
    'second_player': {
        'sign': 'O',
        'human': False,
        'coordinates': {
            'x': None,
            'y': None
        }
    }
}


def print_board():
    border = '-------------'
    print(border)
    print(f'| {cells[0][0]} | {cells[0][1]} | {cells[0][2]} |')
    print(border)
    print(f'| {cells[1][0]} | {cells[1][1]} | {cells[1][2]} |')
    print(border)
    print(f'| {cells[2][0]} | {cells[2][1]} | {cells[2][2]} |')
    print(border)


def get_coordinates(player):
    if player['human']:
        x, y = get_player_coordinates()
    else:
        x, y = get_ai_coordinates()
    player['coordinates']['x'] = x
    player['coordinates']['y'] = y


def get_player_coordinates():
    marker = True
    print('It\'s your turn now!')
    while marker:
        player_x, player_y = input('Input x and y coordinates, separated by comma\n').strip().split(',')
        try:
            player_x = int(player_x) - 1
            player_y = int(player_y) - 1
            if 0 <= player_x <= 2 and 0 <= player_y <= 2:
                print(cells[player_y][player_x])
                if cells[player_y][player_x] == empty_cell:
                    marker = False
                else:
                    print('Sorry, this cell is not empty. Try again.')
                    continue
            else:
                print('There are no such coordinates in the grid.')
                continue
        except ValueError:
            print('One or both of values are invalid.')
            continue
        print('get_player_coordinates works')
        return player_x, player_y


def get_ai_coordinates():
    print('AI turns')
    ai_x = randint(0, 2)
    ai_y = randint(0, 2)
    if cells[ai_y][ai_x] == empty_cell:
        return ai_x, ai_y
    else:
        return get_ai_coordinates()


def make_turn(player):
    x = player['coordinates']['x']
    y = player['coordinates']['y']
    cells[y][x] = player['sign']


def check_win():
    winner_msg = ' is a winner!'
    empty_cell_counter = 0

    for item in cells:
        for element in item:
            if element != empty_cell:
                empty_cell_counter += 1
    if cells[0][0] == cells[1][1] == cells[2][2] and cells[0][0] != empty_cell:
        print('\\ condition')
        print(f'{cells[0][0]}{winner_msg}')
        return True
    if cells[0][2] == cells[1][1] == cells[2][0] and cells[0][2] != empty_cell:
        print(f'{cells[0][2]}{winner_msg}')
        print('/ condition')
        return True
    for column in range(len(cells)):
        if cells[column].count('X') == 3:
            print('- X condition')
            print(f'X {winner_msg}')
            return True
        if cells[column].count('O') == 3:
            print('- O condition')
            print(f'O {winner_msg}')
            return True
        count_x = 0
        count_o = 0
        for row in range(len(cells)):
            if cells[row][column] == 'X':
                count_x += 1
            elif cells[row][column] == 'O':
                count_o += 1
        if count_x == 3:
            print('| X condition')
            print(f'X {winner_msg}')
            return True
        if count_o == 3:
            print('| O condition')
            print(f'O {winner_msg}')
            return True
    else:
        if empty_cell_counter == 9:
            print('It\'s a tie!')
            return True
        else:
            print('Nobody wins now')


def get_players_order():
    valid = False
    while not valid:
        user_input = input('Do you want to be "X" or "O"?\n').lower()
        valid = True
        if user_input == 'x':
            players['first_player']['human'] = True
        elif user_input == 'o':
            players['second_player']['human'] = True
        else:
            valid = False


def main():
    print(border)
    print("Hello, and welcome to the tic-tac-toe!")
    print(border)
    get_players_order()
    first = players['first_player']
    second = players['second_player']
    print_board()

    while True:
        get_coordinates(first)
        print('First player is turning')
        make_turn(first)
        print_board()
        if check_win():
            break
        print('Getting coordinates from second player.')
        get_coordinates(second)
        print('Second player is making a turn.')
        make_turn(second)
        print_board()
        if check_win():
            break


main()
