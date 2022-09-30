import time

from characters.monsters import NPC_Monster
from fight_mechanics.fight_mechanics import Fight
from functions.functions import print_and_pause, clean_terminal


class Events:
    def __init__(self, character):
        self.character = character
        self.rat = NPC_Monster(0, 'Warrior', 'Giant rat')
        self.rat_2 = NPC_Monster(0, 'Warrior', 'Giant rat')

    def print_event_text(self, file_name):
        with open(f'events/events_text/{file_name}.txt') as f:
            for line in f:
                if line[0] == '$':
                    exec(line[2:])
                else:
                    print_and_pause(line.strip())
        time.sleep(2)


class Event1(Events):

    def plot(self):
        self.print_event_text('event_1')

    def debuff(self):
        self.character.strength -= 2
        self.character.cunning -= 2
        self.character.current_hp -= 20
        print_and_pause('You get -2 to cunning and strength.')

    def cunning_test(self):
        if self.character.cunning >= 5:
            print_and_pause('Since you are quite a smart fella,')
            print_and_pause('you realize what equals to')
            print_and_pause('Other beings. Possibly unfriendly.')
            print_and_pause('And you were right.')
            print_and_pause(' There\'s an enormous creaturs sitting in the darkness.')
            self.character.initiative_bonus += 10
            self.rat_encounter()
            self.character.initiative_bonus -= 10
        else:
            print_and_pause('Since you aren\'t the smartest,')
            print_and_pause('you charge forward to get sip of a water.')
            print_and_pause('Sadly, you aren\'t the only one, who wants to drink')
            print_and_pause('But before you realize it, somethings jumps at you')
            self.rat.initiative_bonus += 10
            self.rat_encounter()

    def rat_encounter(self):
        time.sleep(2)
        clean_terminal()
        fight = Fight(self.character, self.rat)
        fight.fight()





