class AnagramChecker:
    def __init__(self, file_path: str):
        with open(file_path) as file:
            self.__words = map(lambda x: x.strip(), file.readlines())

    @staticmethod
    def __is_valid_word(word):
        if word.isalpha():
            return word
        else:
            raise TypeError('Word must be string.')

    @staticmethod
    def __is_anagram(word1, word2):
        word1 = word1.lower().strip()
        word2 = word2.lower().strip()
        if word1 != word2 and len(word1) == len(word2):
            for ch in word1:
                if word1.count(ch) != word2.count(ch):
                    break
            else:
                return True
        return False

    def get_anagrams(self, user_word):
        anagrams = []
        for word in self.__words:
            if self.__is_anagram(user_word, word):
                anagrams.append(word)
        return anagrams

