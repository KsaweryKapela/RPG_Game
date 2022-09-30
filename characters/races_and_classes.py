class Races:

    def __init__(self, character, race_string):
        self.character = character
        self.name = race_string
        self.set_race_bonuses()

    def set_race_bonuses(self):
        if self.name == 'Human':
            self.character.strength -= 1
            self.character.agility -= 1
            self.character.cunning += 2

        elif self.name == 'Elf':
            self.character.strength -= 3
            self.character.agility += 2
            self.character.cunning += 1

        elif self.name == 'Orc':
            self.character.strength += 3
            self.character.cunning -= 3

        else:
            pass


class Classes:

    def __init__(self, character, class_string):
        self.character = character
        self.name = class_string
        self.set_class_bonuses()

    def set_class_bonuses(self):
        if self.name == 'Warrior':
            self.character.strength += 2
            self.character.attack_type = 'melee'
            self.character.main_attribute = 'strength'
            self.character.secondary_attributes = ['agility', 'cunning']

        elif self.name == 'Archer':
            self.character.agility += 2
            self.character.attack_type = 'ranged'
            self.character.main_attribute = 'agility'
            self.character.secondary_attributes = ['strength', 'cunning']

        elif self.name == 'Rogue':
            self.character.cunning += 2
            self.character.attack_type = 'melee'
            self.character.main_attribute = 'cunning'
            self.character.secondary_attributes = ['strength', 'agility']

        else:
            pass

