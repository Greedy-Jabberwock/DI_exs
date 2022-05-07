from main import Dog, print_header
from random import choice

print_header('3: Dogs Domesticated')


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(super().bark())
        self.trained = True

    def play(self, *args):
        dog_names = [x.name for x in args]
        dog_names.append(self.name)
        dog_names = ', '.join(dog_names)
        return f'{dog_names} all play together.'

    def do_a_trick(self):
        if self.trained:
            tricks = ['does a barrel roll.', 'stands on his back legs.',
                      'shakes your hand.', 'plays dead.']
            return f'{self.name} {choice(tricks)}'
        else:
            return f'{self.name} don\'t trained!'


blacksy = PetDog('Blacksy', 3, 7)
gr_nox = PetDog('Gr. Nox', 6, 10)
ripper = PetDog('Ripper', 5, 8)
print(blacksy.do_a_trick())
blacksy.train()
gr_nox.train()
ripper.train()
print(gr_nox.fight(ripper))
print(blacksy.do_a_trick())
print(blacksy.bark())
print(gr_nox.do_a_trick())
print(ripper.play(blacksy, gr_nox))
