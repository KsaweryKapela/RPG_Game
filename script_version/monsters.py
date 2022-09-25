import time

from entity import Entity
from random import randint


class NPC_Monster(Entity):
    def __init__(self, level, monster_class, name):
        super().__init__()
        self.name = name
        self.entity_class = monster_class
        self.level = level
        self.main_attribute = self.classes.main_attribute[self.entity_class]
        self.secondary_attributes = []
        self.set_secondary_attributes()
        self.attribute_points = 3 * self.level
        self.set_class_stats()
        self.set_random_stats()

    def set_class_stats(self):
        for bonus in self.classes.class_bonuses[self.entity_class]:
            exec(bonus)

    def set_secondary_attributes(self):
        for atr in self.classes.main_attribute:
            if self.classes.main_attribute[atr] == self.main_attribute:
                pass
            else:
                self.secondary_attributes.append(self.classes.main_attribute[atr])

    def set_random_stats(self):
        while self.attribute_points:
            roll = randint(1, 4)
            if roll > 2:
                exec(f'self.{self.main_attribute} += 1')
            elif roll == 1:
                exec(f'self.{self.secondary_attributes[0]} += 1')
            elif roll == 2:
                exec(f'self.{self.secondary_attributes[1]} += 1')

            self.attribute_points -= 1
        self.set_stats_from_attributes()

    def print_stats(self):
        print('\n')
        print(f'You see {self.name}, level {self.level}, attack type: {self.attack_type}')
        time.sleep(2)
        print('His stats are:')
        print(f'Strength: {self.attributes["strength"]}, '
              f'Agility: {self.attributes["agility"]}, '
              f'Cunning: {self.attributes["cunning"]}, ')

        time.sleep(2)
        print(f'HP: {self.current_hp}/{self.hp}')

        time.sleep(1)

        print(f'Damage: {self.min_dmg} - {self.max_dmg}')
        time.sleep(1)

        print(f'Armor: {self.armor}')
        time.sleep(1)

        print(f'Hit chance: {self.hit_chance} %')
        time.sleep(1)

        print(f'Crit chance: {self.crit_chance} %')
