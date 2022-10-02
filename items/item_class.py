class Item:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.weight = int
        self.category = str


class Armor(Item):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.category = 'Armor'
        self.dogde_chance = self.armor_stats('dodge_chance')
        self.armor = self.armor_stats('armor')
        self.weight = self.armor_stats('weight')

    def armor_stats(self, string):

        armor_dict = {
            'Pretty clothes': {
                'armor': 0,
                'dodge_chance': 3,
                'weight': 1
            },
            'Old cape': {
                'armor': 1,
                'dodge_chance': 1,
                'weight': 3
            },
            'Leather armor': {
                'armor': 6,
                'dodge_chance': -2,
                'weight': 30
            }
        }

        return armor_dict[self.name][string]


class Edible(Item):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.category = 'Edible'
        self.health_regen = self.food_stats('regen')
        self.edible_during_combat = self.food_stats('in_combat')
        self.weight = self.food_stats('weight')

    def eat_edible(self):
        self.owner.current_healt += self.health_regen

    def food_stats(self, string):

        edible_dict = {
            'Apple': {
                'regen': 5,
                'in_combat': False,
                'weight': 1
            },
            'Roasted chicken': {
                'regen': 10,
                'in_combat': True,
                'weight': 1
            },
            'Health potion': {
                'regen': 20,
                'in_combat': True,
                'weight': 1
            }
        }

        return edible_dict[self.name][string]


class Weapon(Item):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.category = 'Weapon'
        self.damage = self.weapon_stats('damage')
        self.weight = self.weapon_stats('weight')

    def weapon_stats(self, string):
        weapon_dict = {
            'Wooden staff': {
                'damage': 4,
                'weight': 10
            },
            'Dagger': {
                'damage': 5,
                'weight': 3
            },
            'Short sword': {
                'damage': 7,
                'weight': 20
            }
        }

        return weapon_dict[self.name][string]


class Misc(Item):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.category = 'Misc'
        self.function = self.misc_stats('function')
        self.weight = self.misc_stats('weight')

    def misc_stats(self, string):
        misc_dict = {
            'Flint': {
                'function': 'Make fire',
                'weight': 1
            },
            'Ukulele': {
                'function': 'Play music',
                'weight': 10
            },
            'Sleeping-bag': {
                'function': 'Sleep',
                'weight': 15
            },
            'Lockpick': {
                'function': 'Open lock',
                'weight': 0.1
            }
        }

        return misc_dict[self.name][string]
