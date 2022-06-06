import re
import string
import json


class Text:
    def __init__(self, text: str):
        self.text = text.strip()
        self.splitted_text = self.split_text()

    @classmethod
    def from_file(cls, path: str):
        with open(path) as file:
            txt = cls(file.read()) # you can just return here
        return txt

    def split_text(self):
        words = re.findall(r'[a-zA-Z][a-z]+|[aA]', self.text) # you can return a single line
        return words

    def word_frequency(self, word):
        word = word.strip()
        if word in self.splitted_text:
            return self.splitted_text.count(word)
        else:  # it's redundant it will be returned None by default
            return None 

    def unique_words(self):
        return set(self.splitted_text)

    def most_common_word(self):
        counter = {}
        for word in self.unique_words():
            counter[word] = self.text.count(word)
        result = None
        max_value = 0
        for key, value in counter.items():
            if value > max_value:
                result = key
                max_value = value
        return result

    def print_analyse(self, word):
        print('-----------------------------------------------------')
        print(f'Frequency of "{word}": {self.word_frequency(word)}')
        print(f'Unique words in text: {", ".join(self.unique_words())}')
        print(f'Most common word in text: {self.most_common_word()}')
        print('-----------------------------------------------------')


class TextModifications(Text):
    def __init__(self, text):
        super().__init__(text)
        self.text = text
        self.splitted_text = self.split_text()

    def without_punctuation(self):
        p = re.split(f'[{string.punctuation}]', self.text)
        return ' '.join(p)

    def without_stop_words(self):
        with open('stop_words_english.json') as fr:
            stop_words = json.load(fr)
        result = []
        for word in self.splitted_text:
            if word.lower() not in stop_words:
                result.append(word)
        return ' '.join(result)

    def without_special_characters(self):
        special = re.compile('[@_!#$%^&*()<>?/\|}{~:™¦Ђ”]')
        p = re.split(special, self.text)
        return ' '.join(p)


def main():
    text = 'A good book would@@sometimes cost, as much as a good house.  '

    # txt_obj = Text(text)
    # txt_obj.print_analyse(word)

    # file_text = Text.from_file('the_stranger.txt')
    # file_text.print_analyse(word)

    # mod = TextModifications.from_file('the_stranger.txt')
    mod = TextModifications(text)

    print(mod.text)
    print(mod.without_punctuation())
    print(mod.without_stop_words())
    print(mod.without_special_characters())


main()
