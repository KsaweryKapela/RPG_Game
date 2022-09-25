import time
from itertools import cycle
from random import uniform
from rolls import k20


class Fight:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.fight_on = True
        self.initiative_bar = None

    def roll_for_initiative(self):
        if self.player.cunning + k20() > self.monster.cunning + k20():
            self.initiative_bar = cycle([self.player, self.monster])
            print(f'{self.player.name} has reacted faster!')
        else:
            self.initiative_bar = cycle([self.monster, self.player])
            print(f'{self.monster.name} has reacted faster!')

    def turns(self):
        self.roll_for_initiative()
        for fighter in self.initiative_bar:
            if fighter == self.player:
                self.attack(self.player, self.monster)
                if self.monster.current_hp <= 0:
                    time.sleep(1)
                    print(f'You have defeated {self.monster.name}!!')
                    break
            elif fighter == self.monster:
                self.attack(self.monster, self.player)
                if self.player.current_hp <= 0:
                    time.sleep(1)
                    print(f'This is the end of {self.player.name}. {self.monster.name} has defeated you')
                    break

    def attack(self, attacker, attacked):
        time.sleep(1)
        print(f'{attacker.name} attacks {attacked.name} and...')
        time.sleep(1)
        if k20() + attacker.hit_chance > k20() + attacker.armor:
            damage_dealt = round(uniform(attacker.min_dmg, attacker.max_dmg))
            attacked.current_hp -= damage_dealt
            print(f'...blasts him for {damage_dealt}!')
            time.sleep(1)
            if attacked.current_hp <= 0:
                print(f'{attacked.name} has {attacked.current_hp}/{attacked.hp} hp. He is dead.')
            else:
                print(f'{attacked.name} has {round(attacked.current_hp)}/{attacked.hp} hp!')
        else:
            print(f'...misses!')


