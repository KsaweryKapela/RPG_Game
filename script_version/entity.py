class Races:
    def __init__(self):
        self.race_bonuses = {
            'Orc': [
                'self.strength += 3',
                'self.wisdom -=3'
            ],
            'Elf': [
                'self.strength -=3',
                'self.agility += 2',
                'self.wisdom += 1',
            ],
            'Human': [
                'self.strength -= 1',
                'self.agility -= 1',
                'self.wisdom += 2',
            ],
        }


class Classes:

    def __init__(self):
        self.class_bonuses = {
            'Warrior': ['self.strength += 2'],
            'Archer': ['self.agility += 2'],
            'Mage': ['self.wisdom += 2'],
        }

        self.main_attribute = {
            'Warrior': 'strength',
            'Archer': 'agility',
            'Mage': 'wisdom'
        }


class Entity:

    def __init__(self):
        self.char_class = str
        self.race = str
        self.name = str

        self.classes = Classes()
        self.races = Races()

        self.current_hp = int
        self.hp = int

        self.current_mana = int
        self.mana = int

        self.min_dmg = int
        self.max_dmg = int

        self.hit_chance = int
        self.crit_chance = int
        self.armor = int

        self.level = int

        self.strength = 5
        self.agility = 5
        self.wisdom = 5

    @property
    def attributes(self):
        return {'strength': self.strength,
                'agility': self.agility,
                'wisdom': self.wisdom}

    def set_stats_from_attributes(self):
        self.hp = self.strength
        self.current_hp = self.strength
        self.min_dmg = self.attributes[self.classes.main_attribute[self.char_class]]/4
        self.max_dmg = self.attributes[self.classes.main_attribute[self.char_class]]/2
        self.hit_chance = 50 + self.attributes['wisdom']
        self.crit_chance = self.attributes['agility'] + self.attributes['strength']/2
        self.armor = self.attributes['agility']
        self.current_mana = self.attributes['wisdom']
        self.mana = self.attributes['wisdom']



