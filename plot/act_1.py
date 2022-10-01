from events.events import Event1
from functions.functions import print_and_pause, clean_terminal, print_text
import time


class ActOne:
    def __init__(self, character):
        self.character = character

    def introduction(self):
        clean_terminal()
        print_text('plot/text_files/introduction.txt')
        clean_terminal()
        self.character.create_character()

    def entrance_to_the_cave(self):
        clean_terminal()
        print_text('plot/text_files/entrance_to_the_cave.txt')
        clean_terminal()

    def run(self):
        self.introduction()
        self.entrance_to_the_cave()
        event = Event1(self.character)
        event.plot()
