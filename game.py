from characters.player.create_character import create_character
from plot.act_one.act_1 import ActOne
from plot.beginning.benning import opening_text


def run_game():
    opening_text()
    character = create_character()

    first_act = ActOne(character)
    first_act.run()


run_game()
