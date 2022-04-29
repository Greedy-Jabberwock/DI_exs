from random import randint

# ========================== Exercise 1: Double dice ===========================


def throw_until_doubles(throws_doubles):
    is_doubles = False
    throw_dice = (lambda: randint(1, 6))
    while not is_doubles:
        throw = (throw_dice(), throw_dice())
        throws_doubles['all_throws'].append(tuple(throw))
        if throw[0] == throw[1]:
            is_doubles = True
    throws_doubles['total_throws'] += len(throws_doubles['all_throws'])
    return throws_doubles


def main():
    doubles_needed = 100
    all_dices = {
        'all_throws': [],
        'total_throws': 0
    }
    for _ in range(doubles_needed):
        all_dices = throw_until_doubles(all_dices)

    print(f'Total amount of throws, needed to reach 100 doubles:  {all_dices["total_throws"]}')
    average = round(all_dices['total_throws']/len(all_dices['all_throws']), 2)
    print(f'Average count of throws to reach double: {average}')


main()
