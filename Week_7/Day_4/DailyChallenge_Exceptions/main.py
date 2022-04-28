def divide_by_zero(number):
    try:
        print(number/0)
    except ZeroDivisionError:
        print("You're trying to divide by zero? It's possible, but not here.")


divide_by_zero(5)
