from fight_mechanics.fight_mechanics import Fight
from functions.basic_functions import print_and_pause
from functions.input_class import CheckInput


class MonsterEncounter:
    def __init__(self, character, npc):
        self.character = character
        self.npc = npc
        self.plot_device = CheckInput(self.character)
        self.commands = ['Attack', 'Wait', 'Run', 'Look']
        self.special_commands = self.get_special_commands()
        self.commands_dict = {
            'Attack': self.attack_monster,
            'Look': self.look,
            'Run': self.run_away,
            'Tame': self.tame
        }

    def get_special_commands(self):
        if 'Ukulele' in [item.name for item in self.character.eq.items]:
            return ['Tame']
        else:
            return None

    def run(self):
        self.description()
        self.reaction()

    def description(self):
        print_and_pause(f'You see {self.npc.hostility_string} {self.npc.name}.'.capitalize())

    def reaction(self):
        action = self.plot_device.catch_input('Take a closer look at him, attack or run away?',
                                              self.commands, self.special_commands)
        self.commands_dict[action]()

    def attack_monster(self):
        print_and_pause(f'You leap forward an try to attack monster with your {self.character.eq.equipped_weapon.name}')
        fight = Fight(self.character, self.npc)
        fight.fight()

    def look(self):
        pass

    def run_away(self):
        pass

    def tame(self):
        pass