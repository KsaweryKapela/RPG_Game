from characters.races.abstract_char_race import AbstractCharRace


class Rat(AbstractCharRace):
    def __init__(self, npc):
        super().__init__(npc)
        self.type = 'Cave_animal'
        self.name = 'Rat'
        self.hostility = 50
        self.threat = 1
        npc.main_attribute = 'agility'
        npc.secondary_attributes = ['strength', 'cunning']
        self.set_race_bonuses(bonus_strength=-4, bonus_agility=1, bonus_cunning=-3)


class Bear(AbstractCharRace):
    def __init__(self, npc):
        super().__init__(npc)
        self.type = 'Forest_animal'
        self.name = 'Bear'
        self.hostility = 40
        self.threat = 5
        npc.main_attribute = 'strength'
        npc.secondary_attributes = ['agility', 'cunning']

        self.set_race_bonuses(bonus_strength=+5, bonus_agility=1, bonus_cunning=-3)


class Raccoon(AbstractCharRace):
    def __init__(self, npc):
        super().__init__(npc)
        self.type = 'Forest_animal'
        self.name = 'Raccoon'
        self.hostility = 50
        self.threat = 2
        npc.main_attribute = 'agility'
        npc.secondary_attributes = ['strength', 'cunning']
        self.set_race_bonuses(bonus_strength=-3, bonus_agility=3, bonus_cunning=1)


class Hedgehog(AbstractCharRace):
    def __init__(self, npc):
        super().__init__(npc)
        self.type = 'Forest_animal'
        self.name = 'Hedgehog'
        self.hostility = 30
        self.threat = 1
        npc.main_attribute = 'agility'
        npc.secondary_attributes = ['strength', 'cunning']
        self.set_race_bonuses(bonus_strength=-3, bonus_agility=-3, bonus_cunning=-3)


