from random import randint

cells = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
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

win = False


def print_board(cell_values):
    border = '-------------'
    print(border)
    print(f'| {cell_values[0][0]} | {cell_values[0][1]} | {cell_values[0][2]} |')
    print(border)
    print(f'| {cell_values[1][0]} | {cell_values[1][1]} | {cell_values[1][2]} |')
    print(border)
    print(f'| {cell_values[2][0]} | {cell_values[2][1]} | {cell_values[2][2]} |')
    print(border)


def get_coordinates():
    for key, value in players.items():
        if players[key]['human']:
            x, y = get_player_coordinates
        else:
            x, y = get_ai_coordinates
        players[key]['coordinates']['x'] = x
        players[key]['coordinates']['y'] = y


def check_validation(x_coord, y_coord):
    return cells[y_coord][x_coord] == ' '


def make_turn():
    pass


def check_win():
    pass


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
    # print_board(cells)
    # x, y = get_coordinates(current_player)
    # make_turn(x, y, current_player)
    # check_win(cells)

    border = '========================================'
    print(border)
    print("Hello, and welcome to the tic-tac-toe!")
    print(border)
    get_players_order()
    get_coordinates()
    while not win:
        pass


# main()
