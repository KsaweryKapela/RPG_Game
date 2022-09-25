import time

from monsters import NPC_Monster
from player_character import MainCharacter
import os
from fight_mechanics.fight_mechanics import Fight


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
        time.sleep(2)
        print('GET READY TO FIGHT')
        fight = Fight(self.main_character, monster)
        fight.turns()



    def gameplay(self):
        os.system('CLS')
        self.start_game()
        os.system('CLS')
        self.encounter_monster()

    def test(self):
        monster = NPC_Monster(0, 'Warrior', 'Slave')
        main_character = MainCharacter()
        main_character.name = 'Test Hero'
        main_character.entity_class = 'Warrior'
        main_character.set_stats_from_attributes()
        fight = Fight(main_character, monster)
        fight.turns()


gameplay = Gameplay()
gameplay.gameplay()
