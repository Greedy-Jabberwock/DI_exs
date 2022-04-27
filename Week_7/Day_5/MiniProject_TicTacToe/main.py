cells = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


def print_board(cell_values):
    border = '-------------'
    print(border)
    print(f'| {cell_values[0][0]} | {cell_values[0][1]} | {cell_values[0][2]} |')
    print(border)
    print(f'| {cell_values[1][0]} | {cell_values[1][1]} | {cell_values[1][2]} |')
    print(border)
    print(f'| {cell_values[2][0]} | {cell_values[2][1]} | {cell_values[2][2]} |')
    print(border)


def get_coordinates(player):
    pass


def make_turn():
    pass


def check_win():
    pass


def main():
    # print_board(cells)
    # x, y = get_coordinates(current_player)
    # make_turn(x, y, current_player)
    # check_win(cells)
    win = False
    first_player = ''
    second_player = ''
    border = '========================================'
    print(border)
    print("Hello, and welcome to the tic-tac-toe!")
    print(border)
    player = input('Do you want to be "X" or "O"?')



main()
