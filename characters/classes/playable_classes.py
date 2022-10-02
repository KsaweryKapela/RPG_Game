from characters.classes.class_ import Class_
from items.item_class import Weapon, Armor, Misc


class Warrior(Class_):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Warrior'
        self.character.strength += 2
        self.character.main_attribute = 'strength'
        self.character.secondary_attributes = ['agility', 'cunning']
        if self.character.player_char:
            self.give_starting_items()

    def give_starting_items(self):
        sword = Weapon('Short sword', self.character)
        leather_armor = Armor('Leather armor', self.character)
        self.character.eq.add_items(sword, leather_armor)


class Rogue(Class_):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Rogue'
        self.character.agility += 2
        self.character.main_attribute = 'agility'
        self.character.secondary_attributes = ['strength', 'cunning']
        self.give_starting_items()

    def give_starting_items(self):
        dagger = Weapon('Dagger', self.character)
        old_cape = Armor('Old cape', self.character)
        lock_pick = Misc('Lockpick', self.character)
        self.character.eq.add_items(dagger, old_cape, lock_pick)


class Bard(Class_):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Bard'
        self.character.cunning += 2
        self.character.main_attribute = 'cunning'
        self.character.secondary_attributes = ['strength', 'agility']
        self.give_starting_items()

    def give_starting_items(self):
        wooden_staff = Weapon('Wooden staff', self.character)
        pretty_clothes = Armor('Pretty clothes', self.character)
        ukulele = Misc('Ukulele', self.character)
        self.character.eq.add_items(wooden_staff, pretty_clothes, ukulele)
