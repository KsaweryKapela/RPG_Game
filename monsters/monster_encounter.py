from fight_mechanics.fight_mechanics import Fight
from functions.basic_functions import print_and_pause
from functions.input_class import CheckInput
from monsters.monsters_dict import level_differences_dict


class MonsterEncounter:
    def __init__(self, character, npc):
        self.character = character
        self.npc = npc
        self.plot_device = CheckInput(self.character)
        self.commands = ['Attack', 'Wait', 'Avoid', 'Look']
        self.commands_dict = {
            'Attack': self.attack_monster,
            'Look': self.look,
            'Avoid': self.avoid_fight,
            'No': self.stop_encounter
        }
        self.initiative_bonus = 0

    def run(self):
        self.description()
        self.reaction()

    def compare(self):
        strength_difference = self.character.threat - self.npc.threat
        print_and_pause(f'{level_differences_dict[strength_difference]}.')

    def description(self):
        print_and_pause(f'You see {self.npc.name}, {self.npc.hostility_string}.'.capitalize())

    def reaction(self):
        action = self.plot_device.catch_input('Take a closer look at him, attack or avoid fight?',
                                              self.commands)
        self.commands_dict[action]()

    def reaction_2(self):
        self.commands = ['No', 'Attack', 'Look']
        action = self.plot_device.catch_input(
            f'Do you want to take other actions, as animal slowly starts to walk away?',
            self.commands)
        self.commands_dict[action]()

    def attack_monster(self):
        print_and_pause(f'You leap forward an try to attack monster with your {self.character.eq.equipped_weapon.name}')
        self.initiative_bonus += self.character.cunning / 2
        print_and_pause('*You get initiative bonus*')
        self.fight_and_listen()

    def look(self):
        self.npc.print_stats()
        self.compare()

        if self.npc.attacks(self.character.threat):
            print_and_pause(f'As you are taking a look, {self.npc.name} sneakily attacks you!')
            self.initiative_bonus -= self.npc.cunning / 2
            print_and_pause(f'*{self.npc.name} gets initiative bonus*')
            self.fight_and_listen()

        else:
            print_and_pause(f'The {self.npc.name} seems unbothered by your sight.')
            self.reaction_2()

    def avoid_fight(self):
        if self.npc.attacks(self.character.threat, 10):
            print_and_pause(f'Sadly {self.npc.name} attacks you anyways')
            self.fight_and_listen()
        else:
            print_and_pause(f'The {self.npc.name} seems unbothered by you.')
            self.reaction_2()

    def stop_encounter(self):
        print_and_pause(f'{self.npc.name} leaves and you come back to your previous actions.')

    def fight_and_listen(self):
        fight = Fight(self.character, self.npc)
        fight.fight(self.initiative_bonus)
        if fight.fight_outcome == 'Player_surrender':
            print_and_pause(f'{self.npc.name} accepts your surrender and bites into delicious apples from a tree.')
            self.reaction_2()
