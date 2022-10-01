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
        self.armor = int


class Edible(Item):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.health_regen = self.food_stats()[0]
        self.category = 'Edible'
        self.edible_during_combat = self.food_stats()[1]

    def eat_edible(self):
        self.owner.current_healt += self.health_regen

    def food_stats(self):
        edible_dict = {
            'Apple': [5, False],
            'Roasted chicken': [10, True],
            'Health potion': [20, True]
        }

        return edible_dict[self.name]


class Weapon(Item):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.category = 'Weapon'
        self.damage = int


class Misc(Item):
    def __init__(self, name, owner, function=None):
        super().__init__(name, owner)
        self.category = 'Misc'
        self.function = function
