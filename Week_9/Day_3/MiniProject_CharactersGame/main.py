def decorate(fn):
    border = '~' * 60

    def wrapper(*args, **kwargs):
        print(border)
        fn(*args, **kwargs)
        print(border)

    return wrapper


class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10

    @staticmethod
    def is_alive(cls):
        if cls.life <= 0:
            cls.life = 0
            return False
        else:
            return True

    @staticmethod
    def already_dead(cls):
        print(f'{cls.name} is dead.')

    @decorate
    def basic_attack(self, other):
        if not Character.is_alive(self):
            print(f'{self.name} is dead.')
        elif not Character.is_alive(other):
            print(f'Stop it. {other.name} already dead.')
        elif Character.is_alive(self) and Character.is_alive(other):
            print(f'{self.name} attacks {other.name}, '
                  f'and deals {self.attack} damage')
            other.life -= self.attack
            Character.is_alive(other)


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        self.shout()

    def __repr__(self):
        return f'Druid {self.name}:' \
               f'\n\t- Life: {self.life:^13}' \
               f'\n\t- Attack: {self.attack:^10}'

    @decorate
    def shout(self):
        if Character.is_alive(self):
            print(f'{self.name}: "Sacrifice for the nature!"')

    @decorate
    def meditate(self):
        if Character.is_alive(self):
            print(f'Druid {self.name} meditates.\n'
                  f'(Life increased by 10, attack decreased by 2.)')
            self.life += 10
            self.attack -= 2

    @decorate
    def animal_help(self):
        if Character.is_alive(self):
            print(f'Animals helps to {self.name}\n(Attack increased by 5)')

    @decorate
    def fight(self, other):
        if not Character.is_alive(self):
            print(f'{self.name} is dead.')
        elif not Character.is_alive(other):
            print(f'Stop it. {other.name} already dead.')
        elif Character.is_alive(self) and Character.is_alive(other):
            attack_power = round(0.75 * self.life + 0.75 * self.attack)
            print(f'{self.name} fights with {other.name} '
                  f'and deals {attack_power} damage!')
            other.life -= attack_power
            Character.is_alive(other)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.shout()

    def __repr__(self):
        return f'Warrior {self.name}: ' \
               f'\n\t- Life: {self.life:^14}' \
               f'\n\t- Attack: {self.attack:^10}'

    @decorate
    def shout(self):
        print(f'{self.name}: "For the glory! For the honor!"')

    @decorate
    def brawl(self, other):
        if not Character.is_alive(self):
            print(f'{self.name} is dead.')
        elif not Character.is_alive(other):
            print(f'Stop it. {other.name} already dead.')
        elif Character.is_alive(self) and Character.is_alive(other):
            attack_power = self.attack * 2
            self.life += round(self.attack * 0.5)
            other.life -= attack_power
            print(f'{self.name} brawls with {other.name} '
                  f'and deals {attack_power} damage!')
            Character.is_alive(other)

    @decorate
    def train(self):
        if Character.is_alive(self):
            print(f'{self.name} trains.\n(Attack and life increased by 2)')
            self.life += 2
            self.attack += 2

    @decorate
    def roar(self, other):
        if not Character.is_alive(self):
            print(f'{self.name} is dead.')
        elif not Character.is_alive(other):
            print(f'Stop it. {other.name} already dead.')
        elif Character.is_alive(self) and Character.is_alive(other):
            print(f'{self.name} roars to {other.name} '
                  f'and decrease it\'s attack by 3')
            other.attack -= 3


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.shout()

    def __repr__(self):
        return f'Mage {self.name}: ' \
               f'\n\t- Life: {self.life:^13}' \
               f'\n\t- Attack: {self.attack:^10}'

    @decorate
    def shout(self):
        if Character.is_alive(self):
            print(f'{self.name}: "Knowledge gives power. Always."')

    @decorate
    def curse(self, other):
        if not Character.is_alive(self):
            print(f'{self.name} is dead.')
        elif not Character.is_alive(other):
            print(f'Stop it. {other.name} already dead.')
        elif Character.is_alive(self) and Character.is_alive(other):
            print(f'{self.name} curses {other.name} '
                  f'and decrease it\'s attack by 2.')
            other.attack -= 2

    @decorate
    def summon(self):
        if Character.is_alive(self):
            print(f'{self.name} summons the magic creature!\n'
                  f'(Attack increased by 3)')
            self.attack += 3

    @decorate
    def cast_spell(self, other):
        if not Character.is_alive(self):
            print(f'{self.name} is dead.')
        elif not Character.is_alive(other):
            print(f'Stop it. {other.name} already dead.')
        elif Character.is_alive(self) and Character.is_alive(other):
            cast_power = round(self.life / self.attack)
            print(f'{self.name} is casting the spell to attack {other.name}\n'
                  f'Spell deals {cast_power} damage!')
            other.life -= cast_power
            Character.is_alive(other)


def main():
    druid = Druid('Lion Claw')
    warrior = Warrior("Sir Brann")
    mage = Mage('Merlin the Great')

    druid.animal_help()
    warrior.train()
    mage.curse(druid)
    mage.curse(warrior)
    warrior.roar(mage)
    druid.meditate()
    warrior.train()
    warrior.train()
    mage.curse(warrior)
    druid.fight(mage)
    warrior.roar(mage)
    warrior.train()
    druid.fight(warrior)
    print(warrior)
    mage.curse(warrior)
    druid.animal_help()
    warrior.brawl(druid)
    print(druid)
    warrior.brawl(druid)
    druid.meditate()
    print(druid)
    print(mage)
    print(warrior)

main()
