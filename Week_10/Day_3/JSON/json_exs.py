import json
from random import choice

with open('file.json', 'r') as f:
    family = json.load(f)

    print(f'Here some info about {family["firstName"]} {family["lastName"]} children:')
    colors = ['green', 'purple', 'red', 'blue']
    for child in family['children']:
        child['favoriteColor'] = choice(colors)
        print(f'- {child["firstName"]} is {child["age"]} y.o.\t'
              f'Favorite color: {child["favoriteColor"]}')

    with open('file.json', 'w') as f:
        json.dump(family, f, indent=4)





