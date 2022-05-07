# ========================================== PART 1: Quizz ==============================================

"""
What is a class?
    Class is a build-in or user-defined object type data, which can have attributes and methods to create instances
    to operate data.

What is an instance?
    Instance is a non-abstract object of some class, concrete instance of some class.

What is encapsulation?
    Encapsulation is possibility to wrap data within one block and giving restrictions to data to prevent accidentally
    accesses to variables and methods.

What is abstraction?
    Abstraction is an idea about creating classes without concrete realization. It gives a possibility to create
    concrete instances as a copies of an abstract classes. Abstraction describe only most common parameters of class.

What is inheritance?
    Inheritance is a possibility to inherit one classes to another to give an accesses to methods and attributes of
    parent classes (superclasses).

What is multiple inheritance?
    Multiple inheritance gives a possibility to inherit several classes by one class and give all methods and attributes
    of superclasses. But the first of them will be in the highest priority and will override methods and attributes,
    which have same names of attributes or methods.

What is polymorphism?
    Polymorphism is a possibility to override parent's methods or attributes with a child's values, if they have the
    same names.

What is method resolution order or MRO?
    MRO is a method, needs to make a linear list of calls the classes for searching concrete method or value in class
    or his parents. If you try to call method or use a variable of class, the python interpreter will search this
    method or value first in this class, then in his first parent, his first parent, second parent, etc. In necessary
    to prevent errors and usage of the methods and values of the right classes.
"""

# class P: ...
# class X(P): ...
# class O: ...
# class Y(P): ...
# class A(O): ...
# class B(O): ...
# class C(X): ...
# class D(X): ...
# class E(Y): ...
# class K1(A, B, C): ...
# class K2(B, D): ...
# class K3(C, D, E): ...
# class Z(K1, K2, K3): ...
#
# print(Z.mro())

# ===================================== PART 2: Create A Deck Of Cards Class. =====================================
from random import shuffle, randint


class Deck:
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits_images = ['♥', '♦', '♣', '♠']

    def __init__(self):
        self.deck = []
        self.count_of_cards = 0
        for suit in self.suits_images:
            for value in self.values:
                self.deck.append(Card(value, suit))
                self.count_of_cards += 1

    def shuffle_cards(self):
        shuffle(self.deck)

    def print_card(self, card):
        s = card.suit
        v = card.value
        print(f'┌──────────┐\n'
              f'| {s}\t       |\n'
              f'|          |\n'
              f'|    {v}\t   |\n'
              f'|          |\n'
              f'|        {s:^1} |\n'
              f'└──────────┘\n')
        print(f'\nIn deck remain {self.count_of_cards} cards.')

    def deal(self):
        dealing_card = self.deck.pop(randint(0, len(self.deck)-1))
        self.count_of_cards -= 1
        self.print_card(dealing_card)


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f'{self.value:^2} of {self.suit}'


deck = Deck()
deck.shuffle_cards()
deck.deal()
