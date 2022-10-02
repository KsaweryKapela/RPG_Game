from characters.player.create_character import create_character
from events.events import Event1
from functions.basic_functions import print_and_pause, clean_terminal, print_text, check_input, check_input_multiple


class ActOne:
    def __init__(self, character=create_character):
        self.character = character
        self.actions = ['Eq', 'Look', 'Stats', 'Enter']

    def plot(self):
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
            'Eq': self.character.eq.print_eq,
            'Stats': self.character.print_stats,
            'Enter': self.entrance,
            'Look': self.look_around
        }
        action = check_input(f'What now? {self.actions}? ', self.actions)
        if action == 'Enter':
            action_dict[action]()
        else:
            action_dict[action]()
            self.caves_outsides_action()

    def look_around(self):
        print('Theres nothing to do here!')
        self.actions.remove('Look')

    def entrance(self):
        clean_terminal()
        print_text('plot/act_one/text_files/entrance_to_the_cave.txt')
        clean_terminal()
        event = Event1(character=self.character)
        event.plot()


