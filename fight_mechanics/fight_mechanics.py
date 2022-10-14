from random import uniform
from functions.input_class import CheckInput
from functions.rolls import k20, k50
from functions.basic_functions import print_and_pause, is_lucky, is_crit


class Fight:
    def __init__(self, player, npc):
        self.player = player
        self.npc = npc
        self.fight_on = True
        self.plot_device = CheckInput(self.player)
        self.fight_commands = ['Attack', 'Surrender']
        self.fight_dict = {'Attack': self.player_attack,
                           'Surrender': self.player_surrender}
        self.fight_outcome = None

    def roll_for_initiative(self, initiative_bonus=0):
        print_and_pause('*Roll for initiative*')

        if self.player.initiative + k20() + initiative_bonus > self.npc.initiative + k20():
            print_and_pause(f'The {self.npc.name} did not react on time')
            self.player_turn('Attack')

            if is_lucky(self.player.luck):
                print_and_pause(f'... but thanks to his luck, you stumbled!')
                self.npc_turn()
        else:
            print_and_pause(f'{self.npc.name} has reacted faster!')
            self.npc_turn()

            if is_lucky(self.player.luck):
                print_and_pause(f'... but thanks to {self.player.name}\'s luck, {self.npc.name} has slipped!')
                self.player_turn('Attack')

    def player_turn(self, action=None):
        if action is None:
            action = self.plot_device.catch_input('How do you react? Attack, tame or surrender?', self.fight_commands)
        self.fight_dict[action]()
        if self.fight_on:
            self.npc_turn()

    def npc_turn(self):
        if self.npc.attacks(-20):
            self.npc_attack()
        else:
            print_and_pause(f'The {self.npc.name} lies on the ground, as if it wanted to show you how harmless it is.')
            # self.npc.armor_bonus -= 20
            self.npc.hostility -= 20
        if self.fight_on:
            self.player_turn()

    def fight(self, initiative_bonus=0):
        self.roll_for_initiative(initiative_bonus)

        if self.npc.current_hp <= 0:
            print_and_pause(f'You have defeated {self.npc.name}!!')

        if self.player.current_hp <= 0:
            print_and_pause(f'This is the end of {self.player.name}. {self.npc.name} has defeated you')

    def player_attack(self):

        print_and_pause(f'You swing at {self.npc.name} and...')

        if k20() + self.player.hit_chance > k20() + self.npc.armor:
            if is_lucky(self.npc.luck):
                print_and_pause(f'...blast him for...')
                print_and_pause(f'...Nothing. Thanks to his insane luck, {self.npc.name} has survived no injuries',
                                2)

            else:
                damage_dealt = round(uniform(self.player.min_dmg, self.player.max_dmg))
                if is_crit(self.player.crit_chance):
                    print_and_pause('CRITICAL!!!')
                    print_and_pause(f'...obliterate him for {damage_dealt * 2}!')
                    damage_dealt *= 2
                else:
                    print_and_pause(f'...blast him for {damage_dealt}!')
                self.npc.current_hp -= damage_dealt

            if self.npc.current_hp <= 0:
                print_and_pause(f'{self.npc.name} has {self.npc.current_hp}/{self.npc.hp} hp. He is dead.')
                self.fight_on = False
            else:
                print_and_pause(f'{self.npc.name} has {self.npc.current_hp}/{self.npc.hp} hp!')
        else:
            print_and_pause(f'...miss!')

    def npc_attack(self):

        print_and_pause(f'{self.npc.name} attacks you and...')

        if k20() + self.npc.hit_chance > k20() + self.player.armor:
            if is_lucky(self.npc.luck):
                print_and_pause(f'...blasts you for...')
                print_and_pause(f'...Nothing. Thanks to some insane luck, you have survived no injuries',
                                2)

            else:
                damage_dealt = round(uniform(self.npc.min_dmg, self.npc.max_dmg))
                if is_crit(self.npc.crit_chance):
                    print_and_pause('CRITICAL!!!')
                    print_and_pause(f'...obliterates you for {damage_dealt * 2}!')
                    damage_dealt *= 2
                else:
                    print_and_pause(f'...blasts you for {damage_dealt}!')
                self.player.current_hp -= damage_dealt

            if self.player.current_hp <= 0:
                print_and_pause(
                    f'You have {self.player.current_hp}/{self.player.hp} hp. This is the end of your journey.')
                self.fight_on = False
            else:
                print_and_pause(f'You have {self.player.current_hp}/{self.player.hp} hp!')
        else:
            print_and_pause(f'...misses!')

    def player_surrender(self):
        if self.surrender_accepted():
            self.fight_on = False
            self.fight_outcome = 'Player_surrender'
        else:
            # self.player.armor_bonus -= 20
            print_and_pause(f'That only made {self.npc.name} more angry.')
            self.npc.hostility += 20
            self.npc_attack()

    def surrender_accepted(self, surrender_bonus=100):
        result = self.player.threat + k50() + surrender_bonus - self.npc.hostility - self.npc.threat
        if result > 0:
            return True
        else:
            return False
