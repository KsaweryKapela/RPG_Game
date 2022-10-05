import random

from fight_mechanics.fight_mechanics import Fight
from functions.basic_functions import print_text, print_and_pause, clean_terminal
from functions.input_class import CheckInput
from functions.rolls import k100
from items.item_class import Edible
from monsters.monster_encounter import MonsterEncounter
from monsters.monsters_class import NPC_Monster
from monsters.monsters_dict import monsters_dict


class ActOnePointFive:
    def __init__(self, character):
        self.character = character
        self.plot_device = CheckInput(self.character)
        self.actions_1 = ['Harvest', 'Meditate', 'Pick', 'Enter']
        self.actions_1_dictionary = {
            'Harvest': self.harvest_schrooms,
            'Meditate': self.meditate,
            'Pick': self.pick_up_apples,
        }
        self.first_time_apple_tree = True

    def run(self):
        clean_terminal()
        print_text('plot/act_one/text_files/act_1_5.txt')
        self.actions(first_time=True)

    def actions(self, first_time=False):
        if not first_time:
            print_and_pause('Back in the middle of sunny clearing near cave entrance')
        action = self.plot_device.catch_input('Meditate, pick apples, harvest mushrooms or enter cave?', self.actions_1)

        if action == 'Enter':
            return False

        self.actions_1_dictionary[action]()

    def pick_up_apples(self):
        if self.first_time_apple_tree:
            print_and_pause('Great apple tree is full of ripe, red fruits.')
            print_and_pause('You pick one and hide it in your backpack')
            self.first_time_apple_tree = False

        elif not self.first_time_apple_tree:
            self.wild_animal_encounter()
            print_and_pause('You pick up another apple')

        apple = Edible('Apple', self.character)
        self.character.eq.add_items(apple)
        action = self.plot_device.catch_input('Pick another one or go back?',
                                              ['Back', 'Pick'])
        if action == 'Back':
            self.actions()
        else:
            self.pick_up_apples()

    def wild_animal_encounter(self):
        if k100() > 0:
            print_and_pause('Sadly, you aren\'t the only one, who wants to eat apples!', 0)
            animal = random.choice(monsters_dict['Forest_animal'])
            level = random.randint(0, 2)
            monster = NPC_Monster(level, animal)
            encounter = MonsterEncounter(self.character, monster)
            encounter.run()

    def harvest_schrooms(self):
        pass

    def meditate(self):
        pass


