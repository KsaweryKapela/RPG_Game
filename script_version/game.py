from script_version.player_character import MainCharacter


class Gameplay:
    def __init__(self):
        self.main_character = MainCharacter()

    def start_game(self):
        while True:
            if self.main_character.create_character():
                break


gameplay = Gameplay()
gameplay.start_game()
