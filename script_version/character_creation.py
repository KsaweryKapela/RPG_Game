class Races:

    def __init__(self):
        self.race_bonuses = {
            'Orc': ['self.attributes["strength"] += 2', 'self.attributes["wisdom"] -=2'],
            'Elf': ['self.attributes["agility"] += 2', 'self.attributes["strength"] -=2'],
        }


class MainCharacter:

    def __init__(self):
        self.char_clas = str
        self.race = str
        self.name = str

        self.hp = int
        self.dmg = int
        self.armor = int
        self.mana = int

        self.level = 1
        self.money = 0
        self.attribute_points = 10

        self.attributes = {
            'strength': 10,
            'agility': 10,
            'wisdom': 10
        }

    def create_character(self):
        self.name = input('What is your name?').capitalize()
        self.race = input('Choose your race: orc, human or elf').capitalize()
        self.char_clas = input('Choose your character class: mage, warrior or archer').capitalize()

        players_race = Races()
        for bonus in players_race.race_bonuses[self.race]:
            exec(bonus)

    def spend_attribute_points(self):
        for atr in self.attributes:
            while self.attribute_points:
                added_atr = int(input(f'How much points into {atr}? {self.attribute_points} left '))
                if added_atr <= self.attribute_points:
                    print(self.attributes[atr])
                    self.attributes[atr] += added_atr
                    self.attribute_points -= added_atr
                    break

