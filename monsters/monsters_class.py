from random import randint

from characters.classes.classes_dictionary import classes_dict
from characters.entity import Entity
from characters.races.races_dictionary import races_dict
from functions.basic_functions import print_and_pause, range_list
from monsters.monsters_dict import hostility_dict, animal_adjectives_dict


class NPC_Monster(Entity):
    def __init__(self, level, monster_race):
        super().__init__()
        self.level = level
        self.race = monster_race(self)
        self.hostility = self.race.hostility
        self.threat = self.level * self.race.threat
        self.attribute_points = self.threat
        self.name = self.set_monsters_name()
        self.hostility_string = self.get_hostility_string()

        self.set_random_stats()
        self.current_hp = self.hp

    def get_hostility_string(self):
        return hostility_dict[self.hostility]

    def set_monsters_name(self):
        return f'{animal_adjectives_dict[self.threat]} {self.race.name}'

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