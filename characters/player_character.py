from characters.entity import Entity
from functions.functions import print_and_pause, check_input
from characters.races_and_classes import Classes, Races
from functions.functions import clean_terminal


class MainCharacter(Entity):

    def __init__(self):
        super().__init__()
        self.level = 1

    def create_character(self):
        while True:
            if self.char_creation():
                break

    def char_creation(self):
        self.strength = 5
        self.agility = 5
        self.cunning = 5

        self.attribute_points = 6
        self.name = check_input('How are you called? ')

        race = check_input('What\'s your race: human, orc or elf ', ['Human', 'Elf', 'Orc'])
        self.race = Races(self, race)

        class_ = check_input('Tell us your profession: rogue, warrior or archer ',
                             ['Warrior', 'Rogue', 'Archer'])

        self.class_ = Classes(self, class_)

        self.spend_attribute_points()
        self.current_hp = self.hp

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

    def print_stats(self, advanced_stats=False):
        clean_terminal()
        print_and_pause(f'You are {self.name}, {self.race.name}, the {self.class_.name}, level {self.level}')
        print_and_pause('Your stats are:')
        if advanced_stats:
            self.print_advanced_stats()
        else:
            print_and_pause(f'Strength: {self.strength}, '
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
