from itertools import cycle
from random import uniform
from rolls import k20
from functions import print_and_pause, is_lucky, is_crit


class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.fight_on = True
        self.initiative_bar = None

    def roll_for_initiative(self):
        if self.player.cunning + k20() > self.monster.cunning + k20():
            self.initiative_bar = cycle([self.player, self.monster])
            print_and_pause(f'{self.player.name} has reacted faster!')

            if is_lucky(self.player.luck):
                print_and_pause(f'... but thanks to {self.monster.name}\'s luck, {self.player.name} has slipped!')
                self.initiative_bar = cycle([self.monster, self.player])
        else:
            self.initiative_bar = cycle([self.monster, self.player])
            print_and_pause(f'{self.monster.name} has reacted faster!')

            if is_lucky(self.player.luck):
                print_and_pause(f'... but thanks to {self.player.name}\'s luck, {self.monster.name} has slipped!')
                self.initiative_bar = cycle([self.player, self.monster])

    def fight(self):
        self.roll_for_initiative()
        for fighter in self.initiative_bar:

            if fighter == self.player:
                self.attack(self.player, self.monster)
                if self.monster.current_hp <= 0:
                    
                    print_and_pause(f'You have defeated {self.monster.name}!!')
                    break

            elif fighter == self.monster:
                self.attack(self.monster, self.player)
                if self.player.current_hp <= 0:
                    
                    print_and_pause(f'This is the end of {self.player.name}. {self.monster.name} has defeated you')
                    break

    def attack(self, attacker, attacked):
        
        print_and_pause(f'{attacker.name} attacks {attacked.name} and...')
        
        if k20() + attacker.hit_chance > k20() + attacked.armor:
            if is_lucky(attacked.luck):
                print_and_pause(f'...blasts him for...')
                print_and_pause(f'...Nothing. Thanks to his insane luck, {attacked.name} has survived no injuries',
                                2)
                return

            else:
                damage_dealt = round(uniform(attacker.min_dmg, attacker.max_dmg))
                if is_crit(attacker.crit_chance):
                    print_and_pause('CRITICAL!!!')
                    print_and_pause(f'...obliterates him for {damage_dealt*2}!')
                    damage_dealt *= 2
                else:
                    print_and_pause(f'...blasts him for {damage_dealt}!')
                attacked.current_hp -= damage_dealt

            if attacked.current_hp <= 0:
                print_and_pause(f'{attacked.name} has {attacked.current_hp}/{attacked.hp} hp. He is dead.')
            else:
                print_and_pause(f'{attacked.name} has {attacked.current_hp}/{attacked.hp} hp!')
        else:
            print_and_pause(f'...misses!')
