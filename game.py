from characters.player.player_character import MainCharacter
from text.plot.act_1 import ActOne


class Gameplay:
    def __init__(self):
        self.main_character = MainCharacter()
        self.gameplay()

    def gameplay(self):
        first_act = ActOne(self.main_character)
        first_act.run()


gameplay = Gameplay()
