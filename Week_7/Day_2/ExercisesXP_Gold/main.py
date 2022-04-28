from random import random

# --------------------Exercise 1: Temperature Advice -------------------


def get_random_temperature(season):
    celsius_degrees = 0
    if season == 'winter':
        celsius_degrees = round(random(-10, 16), 2)
    elif season == 'spring':
        celsius_degrees = round(random(16, 22), 2)
    elif season == 'summer':
        celsius_degrees = round(random(22, 40), 2)
    elif season == 'autumn':
        celsius_degrees = round(random(-5, 28), 2)
    return celsius_degrees


def main():
    user_season = int(input('Which month is now? (1-12)'))
    season = None
    if 1 <= user_season <= 3:
        season = 'winter'
    elif 4 <= user_season <= 6:
        season = 'spring'
    elif 7 <= user_season <= 9:
        season = 'summer'
    elif 10 <= user_season <= 12:
        season = 'autumn'
    celsius = get_random_temperature(user_season)
    print(f'Temperature right now is {celsius} degrees Celsius.')
    if celsius < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif celsius < 16:
        print("Quite chilly! Don’t forget your coat")
    elif celsius <= 23:
        print("It's perfect weather today! Enjoy!")
    elif celsius <= 32:
        print("There is getting hot outside. Take water on the walk.")
    elif celsius <= 40:
        print("The weather is really hot. Maybe you should stay home today?")

main()