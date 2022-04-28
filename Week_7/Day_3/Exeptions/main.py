my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]

try:
    total = sum(my_list)
    print(total)
except TypeError:
    print("I need only integers in list, without strings!")
