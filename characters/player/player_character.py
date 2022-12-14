from characters.entity import Entity
from characters.player.equipment import Equipment
from functions.basic_functions import print_and_pause, check_input, check_input_multiple
from functions.basic_functions import clean_terminal


class MainCharacter(Entity):

    def __init__(self):
        super().__init__()
        self.player_char = True
        self.level = 1
        self.attribute_points = 6
        self.eq = Equipment(self)

    @property
    def threat(self):
        return 3 + (self.level*3)

    def spend_attribute_points(self):
        for atr in self.attributes:

            while self.attribute_points:
                added_atr = int(check_input_multiple(f'How much points would you like to put into {atr}?\n'
                                                     f'{self.attribute_points} points left ',
                                                     self.attribute_points_range()
                                                     ))
                new_value = getattr(self, atr) + added_atr
                setattr(self, atr, new_value)
                self.attribute_points -= added_atr
                break
        print_and_pause('You have spent your attributes')

    def print_stats(self, advanced_stats=True):
        clean_terminal()
        print(f'You are {self.name}, {self.race.name}, the {self.char_class.name}, level {self.level}')
        print('Your stats are:')
        if advanced_stats:
            self.print_advanced_stats()
        else:
            print(f'Strength: {self.strength}, '
                            f'Agility: {self.agility}, '
                            f'Cunning: {self.cunning}, ')

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

