from characters.player.create_character import create_character
from events.events import Event1
from functions.basic_functions import print_and_pause, clean_terminal, print_text, check_input, check_input_multiple
import time
from strings.entrance_to_cave import CAVE_ENTRANCE


class ActOne:
    def __init__(self):
        clean_terminal()
        print_text('plot/text_files/introduction.txt')
        clean_terminal()
        self.character = create_character()
        self.action_dict = {
            'Eq': self.character.eq.print_eq,
            'Stats': self.character.print_stats,
            'Enter': self.entrance_to_the_cave,
            'Look': self.look_around
        }
        self.actions = ['Eq', 'Look', 'Stats', 'Enter']
        self.caves_outsides()

    def caves_outsides(self):
        clean_terminal()
        action = check_input_multiple(CAVE_ENTRANCE, self.actions)
        if action == 'Enter':
            print('Yo go in!')
        else:
            self.caves_outsides_no2()
  # fix this
    def caves_outsides_no2(self):
        action = check_input(f'What now? {self.actions} ?', self.actions)
        self.action_dict[action]()
        if action == 'Enter':
            print('Yo go in!')
        else:
            self.caves_outsides_no2()

    def look_around(self):
        print('Theres nothing to do here!')
        self.actions.remove('Look')

    def entrance_to_the_cave(self):
        clean_terminal()
        print_text('plot/text_files/entrance_to_the_cave.txt')
        clean_terminal()

