from characters.classes.class_ import Class_


class Warrior(Class_):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Warrior'
        self.character.strength += 2
        self.character.main_attribute = 'strength'
        self.character.secondary_attributes = ['agility', 'cunning']


class Rogue(Class_):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Rogue'
        self.character.agility += 2
        self.character.main_attribute = 'agility'
        self.character.secondary_attributes = ['strength', 'cunning']


class Bard(Class_):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Bard'
        self.character.cunning += 2
        self.character.main_attribute = 'cunning'
        self.character.secondary_attributes = ['strength', 'agility']