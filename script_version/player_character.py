import time

from entity import Entity


class MainCharacter(Entity):

    def __init__(self):
        super().__init__()

    def create_character(self):
        self.level = 1
        self.attribute_points = 6
        self.name = input('What is your name? ').capitalize()
        self.race = input('Choose your race: orc, human or elf ').capitalize()
        self.entity_class = input('Choose your character class: rogue, warrior or archer ').capitalize()

        for bonus in self.classes.class_bonuses[self.entity_class]:
            exec(bonus)

        for bonus in self.races.race_bonuses[self.race]:
            exec(bonus)

        self.spend_attribute_points()
        self.set_stats_from_attributes()
        time.sleep(1)
        print('You have successfully created your character')
        self.print_stats(first_time=True)
        time.sleep(1)
        confirmation = input('Are you happy with your character? Yes/no ')
        if confirmation.lower() == 'no':
            print('Let\'s do it again then')
            return False
        elif confirmation.lower() == 'yes':
            return True

    def spend_attribute_points(self):
        if self.attribute_points == 0:
            print('You have no attribute points to spend')
        else:
            for atr in self.attributes:
                while self.attribute_points:
                    added_atr = int(input(f'How much points would you like to put into {atr}?\n'
                                          f'{self.attribute_points} left '))
                    if added_atr <= self.attribute_points:
                        exec(f'self.{atr} += added_atr')
                        self.attribute_points -= added_atr
                        break
            print('You have spent your attributes')

    def print_stats(self, first_time=False):
        print('\n')
        if first_time:
            time.sleep(2)
        print(f'You are {self.name}, {self.race}, the {self.entity_class}, level {self.level}')
        if first_time:
            time.sleep(2)
            print('Your stats are:')
        print(f'Strength: {self.attributes["strength"]}, '
              f'Agility: {self.attributes["agility"]}, '
              f'Cunning: {self.attributes["cunning"]}, ')

        if self.attribute_points > 0:
            print(f'You can still spend {self.attribute_points} attribute points')

        if first_time:
            time.sleep(2)
        print(f'HP: {self.current_hp}/{self.hp}')

        if first_time:
            time.sleep(1)
        print(f'Damage: {self.min_dmg} - {self.max_dmg}')
        if first_time:
            time.sleep(1)
        print(f'Armor: {self.armor}')
        if first_time:
            time.sleep(1)
        print(f'Hit chance: {self.hit_chance} %')
        if first_time:
            time.sleep(1)
        print(f'Crit chance: {self.crit_chance} %')

    def level_up(self):
        print('You have leveled up!')
        self.attribute_points += 3
        self.spend_attribute_points()
