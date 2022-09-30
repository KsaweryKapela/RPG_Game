from events.events import Event1
from functions.functions import print_and_pause, clean_terminal
import time
from functions.functions import print_text


class ActOne:
    def __init__(self, character):
        self.character = character


    def introduction(self):
        clean_terminal()
        print_text('introduction')
        clean_terminal()
        self.character.create_character()

    def entrance_to_the_cave(self):
        clean_terminal()
        print_text('entrance_to_the_cave')
        clean_terminal()

    def run(self):
        self.introduction()
        self.entrance_to_the_cave()
        event = Event1(self.character)
        event.plot()
