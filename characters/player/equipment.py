import pandas as pd
from items.item_class import Misc
from functions.basic_functions import print_and_pause, clean_terminal


def if_not_empty_print(dataframe):
    if not dataframe.empty:
        print(dataframe, '\n')


class Equipment:
    def __init__(self, player):
        self.player = player
        self.items = {}
        self.give_starting_items()
        self.equipped_weapon = None
        self.equipped_armor = None

    @property
    def weapons(self):
        return {item: value for item, value in self.items.items() if item.category == 'Weapon'}

    @property
    def armors(self):
        return {item: value for item, value in self.items.items() if item.category == 'Armor'}

    @property
    def edibles(self):
        return {item: value for item, value in self.items.items() if item.category == 'Edible'}

    @property
    def misc(self):
        return {item: value for item, value in self.items.items() if item.category == 'Misc'}

    @property
    def sum_weight(self):
        return sum(item.weight for item in self.items)

    def add_items(self, *args):
        for arg in args:
            if arg.name in self.items.keys():
                self.items[arg] += 1
            else:
                self.items[arg] = 1

    def give_starting_items(self):
        flint = Misc('Flint', self.player)
        night_bag = Misc('Sleeping-bag', self.player)
        self.add_items(flint, night_bag)

    def print_eq(self):
        weapons = {
                 'Weapons': [item.name for item in self.weapons.keys()],
                 'Damage': [item.damage for item in self.weapons.keys()],
                 'Weight': [item.weight for item in self.weapons.keys()],
                 'Type': [item.category for item in self.weapons.keys()],
                 }

        weapons_dataframe = pd.DataFrame(data=weapons)\
            .set_index('Weapons')

        armors = {
                 'Armors': [item.name for item in self.armors.keys()],
                 'Armor': [item.armor for item in self.armors.keys()],
                 'Dodge': [item.dogde_chance for item in self.armors.keys()],
                 'Weight': [item.weight for item in self.armors.keys()],
                 'Type': [item.category for item in self.armors.keys()],
                 }

        armors_dataframe = pd.DataFrame(data=armors).set_index('Armors')

        edible = {
                 'Edibles': [item.name for item in self.edibles.keys()],
                 'Regen': [item.health_regen for item in self.edibles.keys()],
                 'In combat': [item.edible_during_combat for item in self.edibles.keys()],
                 'Weight': [item.weight for item in self.edibles.keys()],
                 'Type': [item.category for item in self.edibles.keys()],
                 }

        edible_dataframe = pd.DataFrame(data=edible)\
            .set_index('Edibles')

        misc = {
                 'Misc': [item.name for item in self.misc.keys()],
                 'Function': [item.function for item in self.misc.keys()],
                 'Weight': [item.weight for item in self.misc.keys()],
                 'Type': [item.category for item in self.misc.keys()],
                 }

        misc_dataframe = pd.DataFrame(data=misc)\
            .set_index('Misc')

        clean_terminal()
        if_not_empty_print(weapons_dataframe)
        if_not_empty_print(armors_dataframe)
        if_not_empty_print(edible_dataframe)
        if_not_empty_print(misc_dataframe)

