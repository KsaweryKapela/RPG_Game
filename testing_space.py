from characters.classes.classes_dictionary import classes_dict
from characters.monsters import NPC_Monster
from characters.player.player_character import MainCharacter
from characters.races.races_dictionary import races_dict
from fight_mechanics.fight_mechanics import Fight
from items.item_class import Misc
from plot.act_one.act_1 import ActOne


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
    # rat = NPC_Monster(0, 'Warrior', 'Rat')
    # fight = Fight(character, rat)
    # fight.fight()
    sleeping_bag = Misc('Sleeping-bag', character)
    sleeping_bag_2 = Misc('Sleeping-bag', character)
    character.eq.add_items(sleeping_bag, sleeping_bag_2)
    first_act = ActOne(character)
    first_act.caves_outsides_action()


run_game()
