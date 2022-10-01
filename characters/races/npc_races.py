from characters.races.race import Race


class Rat(Race):
    def __init__(self, npc):
        super().__init__(npc)
        self.name = 'Rat'
        self.set_race_bonuses(bonus_strength=-4, bonus_agility=1, bonus_cunning=-3)
