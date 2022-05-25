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
        self.class_name = self.__class__.__name__

    @staticmethod
    def is_alive(cls):
        if cls.life <= 0:
            cls.life = 0
            return False
        else:
            return True

    @staticmethod
    def already_dead(cls):
        print(f'{cls.class_name} {cls.name} is dead.')

    @staticmethod
    def check_both_death(cls, other):
        if not Character.is_alive(cls):
            Character.already_dead(cls)
            return False
        elif not Character.is_alive(other):
            Character.already_dead(other)
            return False
        else:
            return True

    @decorate
    def basic_attack(self, other):
        if Character.check_both_death(self, other):
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
        else:
            Character.already_dead(self)

    @decorate
    def meditate(self):
        if Character.is_alive(self):
            print(f'Druid {self.name} meditates.\n'
                  f'(Life increased by 10, attack decreased by 2.)')
            self.life += 10
            self.attack -= 2
        else:
            Character.already_dead(self)

    @decorate
    def animal_help(self):
        if Character.is_alive(self):
            print(f'Animals helps to {self.name}\n(Attack increased by 5)')
        else:
            Character.already_dead(self)

    @decorate
    def fight(self, other):
        if Character.check_both_death(self, other):
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
        if Character.is_alive(self):
            print(f'{self.name}: "For the glory! For the honor!"')
        else:
            print(f'{self.class_name} {self.name} is dead.')

    @decorate
    def brawl(self, other):
        if Character.check_both_death(self, other):
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
        else:
            print(f'{self.class_name} {self.name} is dead.')

    @decorate
    def roar(self, other):
        if Character.check_both_death(self, other):
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
        else:
            print(f'{self.class_name} {self.name} is dead.')

    @decorate
    def curse(self, other):
        if Character.check_both_death(self, other):
            print(f'{self.name} curses {other.name} '
                  f'and decrease it\'s attack by 2.')
            other.attack -= 2

    @decorate
    def summon(self):
        if Character.is_alive(self):
            print(f'{self.name} summons the magic creature!\n'
                  f'(Attack increased by 3)')
            self.attack += 3
        else:
            Character.already_dead(self)

    @decorate
    def cast_spell(self, other):
        if Character.check_both_death(self, other):
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
    mage.curse(warrior)
    druid.animal_help()
    warrior.brawl(druid)
    warrior.brawl(druid)
    druid.meditate()
    warrior.train()
    mage.curse(warrior)
    mage.basic_attack(warrior)
    warrior.brawl(mage)
    print(druid)
    print(mage)
    print(warrior)


main()
