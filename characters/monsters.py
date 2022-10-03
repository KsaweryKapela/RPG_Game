from random import randint

from characters.classes.classes_dictionary import classes_dict
from characters.entity import Entity
from characters.races.races_dictionary import races_dict
from functions.basic_functions import print_and_pause


class NPC_Monster(Entity):
    def __init__(self, level, monster_class, monster_race, name=None):
        super().__init__()
        self.name = name if name else monster_race
        self.player_char = False
        self.race = races_dict(monster_race)(self)
        self.class_ = classes_dict(monster_class)(self)
        self.level = level
        self.attribute_points = 3 * self.level
        self.set_random_stats()
        self.current_hp = self.hp

    def set_random_stats(self):
        while self.attribute_points:
            roll = randint(1, 4)
            if roll > 2:
                new_value = getattr(self, str(self.main_attribute)) + 1
                setattr(self, str(self.main_attribute), new_value)

            elif roll == 1:
                new_value = getattr(self, str(self.secondary_attributes[0])) + 1
                setattr(self, str(self.secondary_attributes[0]), new_value)
            elif roll == 2:
                new_value = getattr(self, str(self.secondary_attributes[1])) + 1
                setattr(self, str(self.secondary_attributes[1]), new_value)

            self.attribute_points -= 1

    def print_stats(self, more_stats=True):
        print_and_pause(f'You see {self.name}, level {self.level}, attack type: {self.attack_type}')
        if more_stats:
            print_and_pause('His stats are:')
            self.print_advanced_stats()
