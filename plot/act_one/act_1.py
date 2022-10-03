from characters.player.create_character import create_character
from events.events import Event1
from functions.basic_functions import print_and_pause, clean_terminal, print_text, check_input, check_input_multiple
from functions.input_class import CheckInput
from plot.act_one.act_1_5 import actOnePointFive


class ActOne:
    def __init__(self, character=create_character):
        self.character = character
        self.plot_device = CheckInput(self.character)
        self.actions = ['Look', 'Enter']
        self.act_1_5 = actOnePointFive(self.character)

    def run(self):
        clean_terminal()
        print_text('plot/act_one/text_files/introduction.txt')
        clean_terminal()
        self.character = self.character()
        self.caves_outsides()

    def caves_outsides(self):
        clean_terminal()
        print_text('plot/act_one/text_files/before_entering_cave.txt')
        self.caves_outsides_action()

    def caves_outsides_action(self):
        action_dict = {
            'Enter': self.entrance,
            'Look': self.look_around
        }

        action = self.plot_device.catch_input(f'What now would you like to do now?', self.actions)
        print(action)
        action_dict[action]()

    def look_around(self):
        self.act_1_5.run()
        self.caves_outsides_action()

    def entrance(self):
        clean_terminal()
        print_text('plot/act_one/text_files/entrance_to_the_cave.txt')
        clean_terminal()
        event = Event1(character=self.character)
        event.plot()


