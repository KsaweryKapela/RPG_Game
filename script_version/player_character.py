from entity import Entity
from functions import print_and_pause, check_input
from script_version.races_and_classes import Classes, Races


class MainCharacter(Entity):

    def __init__(self):
        super().__init__()

    def create_character(self):
        self.level = 1
        self.attribute_points = 6
        self.name = check_input('What is your name? ')

        race = check_input('Choose your race: human, orc or elf ', ['Human', 'Elf', 'Orc'])
        self.race = Races(self, race)

        class_ = check_input('Choose your character class: rogue, warrior or archer ',
                             ['Warrior', 'Rogue', 'Archer'])

        self.class_ = Classes(self, class_)

        self.spend_attribute_points()
        self.current_hp = self.hp

        print_and_pause('You have successfully created your character')
        self.print_stats()
        confirmation = check_input('Are you happy with your character? Yes/no ',
                                   ['Yes', 'No', 'Y', 'N'])
        if confirmation == 'No':
            print_and_pause('Let\'s do it again then')
            return False
        elif confirmation == 'Yes':
            return True

    def spend_attribute_points(self):
        for atr in self.attributes:

            while self.attribute_points:
                added_atr = int(check_input(f'How much points would you like to put into {atr}?\n'
                                            f'{self.attribute_points} left ',
                                            self.attribute_points_range()
                                            ))
                new_value = getattr(self, atr) + added_atr
                setattr(self, atr, new_value)
                self.attribute_points -= added_atr
                break
        print_and_pause('You have spent your attributes')

    def print_stats(self):
        print_and_pause(f'You are {self.name}, {self.race.name}, the {self.class_.name}, level {self.level}')
        print_and_pause('Your stats are:')
        self.print_advanced_stats()

    def level_up(self):
        print_and_pause('You have leveled up!')
        self.attribute_points += 3
        self.spend_attribute_points()

    def attribute_points_range(self):
        range_list = []
        number_of_points = self.attribute_points
        for point in range(0, number_of_points + 1):
            range_list.append(str(point))
        return range_list
