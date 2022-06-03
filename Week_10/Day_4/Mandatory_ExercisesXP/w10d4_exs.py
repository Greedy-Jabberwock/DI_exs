import json
from random import choice
from helper import header


def get_words_from_file():
    try:
        with open('sample.txt') as file_obj:
            return file_obj.readlines()
    except FileNotFoundError:
        print('File not found.')


words = get_words_from_file()


def get_random_sentence(length):
    result = ' '.join([choice(words).strip().lower() for _ in range(length)])
    return result.capitalize() + '.'


def make_exercise2():
    sample_json = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""

    info = json.loads(sample_json)
    salary = info['company']['employee']['payable']['salary']
    print(salary)
    info['company']['employee']['birth_date'] = None

    with open('exs_2.json', 'w') as file:
        json.dump(info, file, indent=3)


def main():
    # Exercise 1
    header('Exercise 1: Random Sentence Generator')
    print('Hello. This script is giving you random sentence with the length which you want. Let\'s try!')
    while True:
        answer = int(input('Give me a length of the random sentence, between 2-20: '))
        if 2 <= answer <= 20:
            print(get_random_sentence(answer))
            break
        else:
            raise ValueError('I need a number between 2 and 20.')

    # Exercise 2
    header('Exercise 2: Working With JSON')
    make_exercise2()


main()
