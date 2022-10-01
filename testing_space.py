from characters.player.create_character import create_character
from characters.player.player_character import MainCharacter
from events.events import Event1


class Gameplay:
    # def __init__(self):
    #     # self.main_character = MainCharacter()

    def test_creating_char(self):
        main_character = create_character()
        print(main_character.name)
        print(main_character.strength)

    # def create_test_char(self):
    #     self.main_character.name = 'Testing_character'
    #     self.main_character.race = Races(self.main_character, 'Orc')
    #     self.main_character.class_ = Classes(self.main_character, 'Warrior')
    #     self.main_character.attribute_points = 6
    #     self.main_character.strength += 3
    #     self.main_character.agility += 1
    #     self.main_character.cunning += 1
    #     self.main_character.current_hp = self.main_character.hp


    def gameplay(self):
        self.create_test_char()
        event = Event1(self.main_character)
        event.plot()


gameplay = Gameplay()
gameplay.gameplay()

