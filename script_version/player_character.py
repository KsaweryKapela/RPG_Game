import time

from entity import Entity
from functions import print_and_pause
from script_version.races_and_classes import Classes, Races


class MainCharacter(Entity):

    def __init__(self):
        super().__init__()

    def create_character(self):
        self.level = 1
        self.attribute_points = 6
        self.name = input('What is your name? ').capitalize()
        self.race = input('Choose your race: orc, human or elf ').capitalize()
        self.entity_class = input('Choose your character class: rogue, warrior or archer ').capitalize()

        race = Races(self)
        entity_class = Classes(self)

        self.spend_attribute_points()
        self.current_hp = self.hp

        print_and_pause('You have successfully created your character')
        self.print_stats()
        confirmation = input('Are you happy with your character? Yes/no ')
        if confirmation.lower() == 'no':
            print_and_pause('Let\'s do it again then')
            return False
        elif confirmation.lower() == 'yes':
            return True

    def spend_attribute_points(self):
        for atr in self.attributes:

            while self.attribute_points:
                added_atr = int(input(f'How much points would you like to put into {atr}?'
                                      f'{self.attribute_points} left '))
                if added_atr <= self.attribute_points:
                    new_value = getattr(self, atr) + added_atr
                    setattr(self, atr, new_value)
                    self.attribute_points -= added_atr
                    break
        print_and_pause('You have spent your attributes')

    def print_stats(self):
        print_and_pause(f'You are {self.name}, {self.race}, the {self.entity_class}, level {self.level}')
        print_and_pause('Your stats are:')
        self.print_advanced_stats()

    def level_up(self):
        print_and_pause('You have leveled up!')
        self.attribute_points += 3
        self.spend_attribute_points()
