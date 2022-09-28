class Races:

    def __init__(self, character):
        self.character = character
        self.set_race_bonuses()

    def set_race_bonuses(self):
        if self.character.race == 'Human':
            self.character.strength -= 1
            self.character.agility -= 1
            self.character.cunning += 2

        elif self.character.race == 'Elf':
            self.character.strength -= 3
            self.character.agility += 2
            self.character.cunning += 1

        elif self.character.race == 'Orc':
            self.character.strength += 3
            self.character.cunning -= 3


class Classes:

    def __init__(self, character):
        self.character = character
        self.set_class_bonuses()

    def set_class_bonuses(self):
        if self.character.entity_class == 'Warrior':
            self.character.strength += 2
            self.character.attack_type = 'melee'
            self.character.main_attribute = 'strength'

        elif self.character.entity_class == 'Archer':
            self.character.agility += 2
            self.character.attack_type = 'ranged'
            self.character.main_attribute = 'agility'

        elif self.character.entity_class == 'Rogue':
            self.character.cunning += 2
            self.character.attack_type = 'melee'
            self.character.main_attribute = 'cunning'
