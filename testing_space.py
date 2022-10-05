from random import random

from characters.classes.classes_dictionary import classes_dict
from characters.player.player_character import MainCharacter
from characters.races.npc_races import Hedgehog, Bear
from characters.races.races_dictionary import races_dict
from fight_mechanics.fight_mechanics import Fight
from monsters.monsters_class import NPC_Monster
from plot.act_one.act_1 import ActOne
from plot.act_one.act_1_5 import ActOnePointFive


def create_test_char():
    character = MainCharacter()
    character.name = 'Test Character'
    character.race = races_dict('Human')(character)
    character.class_ = classes_dict('Bard')(character)
    character.strength += 1
    character.agility += 2
    character.cunning += 3
    character.attribute_points = 0
    character.current_hp = character.hp
    return character


def run_game():
    character = create_test_char()
    act_1_5 = ActOnePointFive(character)
    act_1_5.wild_animal_encounter()


    #
    # first_act = ActOne(character)
    # first_act.caves_outsides_action()


run_game()
