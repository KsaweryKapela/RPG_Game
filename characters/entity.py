from functions.basic_functions import print_and_pause


class Entity:

    def __init__(self):
        self.name = str

        self.attack_type = str
        self.current_hp = int

        self.level = int
        self.player_char = None
        self.class_ = None
        self.race = None

        self.eq = None

        self.attribute_points = 0

        self.strength = 5
        self.agility = 5
        self.cunning = 5

        self.main_attribute = str
        self.secondary_attributes = []

        self.initiative_bonus = 0

    @property
    def attributes(self):
        return {'strength': self.strength,
                'agility': self.agility,
                'cunning': self.cunning,
                }

    @property
    def max_capacity(self):
        return self.strength * 10

    @property
    def current_capacity(self):
        return self.max_capacity - self.eq.sum_weight()

    @property
    def hp(self):
        return self.strength * 10

    @property
    def min_dmg(self):
        return round(self.attributes[self.main_attribute] / 4 * 10)

    @property
    def max_dmg(self):
        return round(self.attributes[self.main_attribute] / 2 * 10)

    @property
    def hit_chance(self):
        return self.cunning

    @property
    def crit_chance(self):
        return self.agility

    @property
    def dodge_chance(self):
        return self.agility

    @property
    def initiative(self):
        initiative = self.cunning + self.initiative_bonus
        return initiative

    @property
    def armor(self):
        return self.strength

    @property
    def luck(self):
        return round(self.cunning / 4)

    def print_advanced_stats(self):
        print(f'Strength: {self.strength}, '
                        f'Agility: {self.agility}, '
                        f'Cunning: {self.cunning}, ')
        if self.attribute_points > 0:
            print(f'You can still spend {self.attribute_points} attribute points')
        print(f'HP: {self.current_hp}/{self.hp}')
        print(f'Damage: {self.min_dmg} - {self.max_dmg}')
        print(f'Armor: {self.armor}')
        print(f'Hit bonus: {self.hit_chance} %')
        print(f'Dodge bonus: {self.dodge_chance} %')
        print(f'Crit chance: {self.crit_chance} %')
        print(f'Luck chance: {self.luck} %')
