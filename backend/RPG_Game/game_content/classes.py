
class Character:
    
    def __init__(self):

        self.hp = int
        self.dmg = int
        self.armor = int
        self.mana = int
        
        self.level = 1
        self.money = 0
        self.attribute_points = 10
        self.attributes = {"strength": 0,
                           "agility": 0,
                           "wisdom": 0}

    def update_stats(self, stats_json):
        spent_points = sum(stats_json[stat] for stat in stats_json)

        if spent_points > self.attribute_points:
            print('CHEATER')
            return False

        for stat in stats_json:
            self.attributes[stat] += stats_json[stat]

        self.attribute_points -= spent_points

