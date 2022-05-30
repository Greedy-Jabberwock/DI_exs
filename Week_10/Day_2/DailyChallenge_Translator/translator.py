from python_translator import Translator

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
result = {}
translator = Translator()
for word in french_words:
    result[word] = translator.translate(word, 'english', 'french')

for key, value in result.items():
    print(f'{key} : {value}')
