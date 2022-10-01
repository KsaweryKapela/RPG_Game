class Item:
    def __init__(self):
        self.name: str
        self.weight = int
        self.category = str
        self.owner = str


class Armor(Item):
    def __init__(self):
        super().__init__()
        self.category = 'Armor'
        self.armor = int


class Edible(Item):
    def __init__(self, name, owner):
        super().__init__()
        self.name = name
        self.health_regen = self.food_stats()[0]
        self.category = 'Edible'
        self.owner = owner
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
    def __init__(self):
        super().__init__()
        self.category = 'Weapon'
        self.damage = int


class Misc(Item):
    def __init__(self, name, function=None):
        super().__init__()
        self.category = 'Misc'
        self.name = name
        self.function = function
