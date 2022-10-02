from items.item_class import Misc
from functions.basic_functions import print_and_pause


class Equipment:
    def __init__(self, player):
        self.player = player
        self.items = {}
        self.give_starting_items()
        self.equipped_weapon = None
        self.equipped_armor = None

    @property
    def sum_weight(self):
        return sum(item.weight for item in self.items)

    def add_items(self, *args):
        for arg in args:
            if arg.name in self.items.keys():
                self.items[arg.name] += 1
            else:
                self.items[arg.name] = 1

    def give_starting_items(self):
        flint = Misc('Flint', self.player)
        night_bag = Misc('Sleeping-bag', self.player)
        self.add_items(flint, night_bag)

    def print_eq(self):
        # fix this
        for item, number in self.items.items():
            print_and_pause((' '.join(str((item, None if number == 1 else f' x {number}')))))
