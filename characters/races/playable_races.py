from characters.races.abstract_char_race import AbstractCharRace

class Human(AbstractCharRace):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Human'
        self.set_race_bonuses(bonus_strength=-1, bonus_agility=-1, bonus_cunning=2)


class Elf(AbstractCharRace):
    def __init__(self, character):
        super().__init__(character)
        self.name = 'Elf'
        self.set_race_bonuses(bonus_strength=-2, bonus_agility=2, bonus_cunning=0)


class Orc(AbstractCharRace):
    def __init__(self, character):
        super().__init__(character)
        self.character = character
        self.name = 'Orc'
        self.set_race_bonuses(bonus_strength=3, bonus_agility=0, bonus_cunning=-3)
