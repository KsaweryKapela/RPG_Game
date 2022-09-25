import time

from script_version.monsters import NPC_Monster
from script_version.player_character import MainCharacter


class Gameplay:
    def __init__(self):
        self.main_character = MainCharacter()

    def start_game(self):
        while True:
            if self.main_character.create_character():
                break

    def encounter_monster(self):
        monster = NPC_Monster(0, 'Warrior', 'Slave')
        monster.print_stats()
        time.sleep(1)
        print('ARE YOU READY TO FIGHT???')

    def gameplay(self):
        self.start_game()
        self.encounter_monster()


gameplay = Gameplay()
gameplay.gameplay()
