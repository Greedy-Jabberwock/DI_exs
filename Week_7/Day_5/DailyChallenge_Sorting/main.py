sequence = input('Enter words, separated by comma:\n').split(',')
print(sequence)


def sort_list(words):
    sorted_words = []
    biggest = ''
    while len(sorted_words) != len(words):
        for index, word in enumerate(words):
            if biggest < word:
                biggest = word
        words[words.index(biggest)] = ''
        sorted_words.append(biggest)
        biggest = ''
    sorted_words.reverse()
    print(sorted_words)


sort_list(sequence)
