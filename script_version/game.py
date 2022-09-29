from monsters import NPC_Monster
from player_character import MainCharacter
import os
from fight_mechanics.fight_mechanics import Fight
from functions import print_and_pause


class Gameplay:
    def __init__(self):
        self.main_character = MainCharacter()

    def start_game(self):
        while True:
            if self.main_character.create_character():
                break

    def encounter_monster(self):
        monster = NPC_Monster(0, 'Archer', 'Skeleton Archer')
        monster.print_stats()
        print_and_pause('GET READY TO FIGHT')
        fight = Fight(self.main_character, monster)
        fight.fight()

    def gameplay(self):
        self.start_game()
        self.encounter_monster()


gameplay = Gameplay()
gameplay.gameplay()
