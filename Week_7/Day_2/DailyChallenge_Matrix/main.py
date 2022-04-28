matrix = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]


def solve_matrix(some_matrix):
    hidden_message = ""
    rows = len(some_matrix[0])
    columns = len(some_matrix)
    for row in range(rows):
        for column in range(columns):
            el = some_matrix[column][row]
            if el.isalpha():
                hidden_message += el
            elif hidden_message.endswith(' '):
                continue
            else:
                hidden_message += ' '
    return hidden_message.strip()


message = solve_matrix(matrix)
print(message)
