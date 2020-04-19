from abc import ABC
from random import randint, randrange, choice, sample


names = [
    'Aganos', 'Arbiter', 'ARIA', 'Black Orchid', 'Chief Thunder',
    'Cinder', 'Eyedol', 'Eagle', 'Fulgore', 'Gargos',
    'General RAAM', 'Glacius', 'Hisako', 'Jago', 'Kan-Ra',
    'Kilgore', 'Kim Wu', 'Maya', 'Mira', 'Omen'
]


def main():
    fighters = [choice((Paladin, Warrior))(name) for name in sample(names, 10)]
    while len(fighters) > 1:
        attacker, defender = sample(fighters, 2)
        damage = defender.attack_damage(attacker.attack)
        print(f'{attacker.name} наносит удар по {defender.name} на {damage} урона')
        if defender.hp <= 0:
            print(f'{defender.name} побежден')
            fighters.remove(defender)
        else:
            print(f'У {defender.name} осталось {defender.hp}hp')
    print(f'Победитель битвы на арене: {fighters[0].name}')


class Thing:
    def __init__(self):
        self.name = choice(['armor', 'weapon', 'shield'])
        self.defence = randint(0, 10)
        self.power = randint(0, 50)
        self.hp = randint(0, 50)


class Person(ABC):
    def __init__(self, name):
        self.name = name
        self.hp = randrange(50, 200, 10)
        self.attack = randint(1, 100)
        self.defence = randrange(0, 50, 10)
        self.things = [Thing() for i in range(randint(1, 4))]
        self.finalProtection = self.defence + self.set_things()

    def set_things(self):
        self.hp += sum(thing.hp for thing in self.things)
        self.attack += sum(thing.power for thing in self.things)
        protection = sum(thing.defence for thing in self.things)
        return protection

    def attack_damage(self, attack):
        damage = round(attack - attack * (self.finalProtection / 100))
        self.hp -= damage
        return damage


class Paladin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.hp *= 2
        self.defence *= 2
        self.class_name = 'Paladin'


class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.attack *= 2
        self.class_name = 'Warrior'


if __name__ == '__main__':
    main()
