from characters.classes.classes_dictionary import classes_dict
from characters.player.player_character import MainCharacter
from characters.races.races_dictionary import races_dict
from functions.basic_functions import check_input, print_and_pause


def create_character():
    character = MainCharacter()
    character.name = check_input('How are you called? ')

    race = check_input('What\'s your race: human, orc or elf ',
                       ['Human', 'Elf', 'Orc'])

    character.race = races_dict(race)(character)

    class_ = check_input('Are you a warrior, rogue or a bard? ',
                         ['Warrior', 'Rogue', 'Bard'])

    character.class_ = classes_dict(class_)(character)

    print_and_pause('There are three main attributes: Strength, Agility and Cunning')
    character.spend_attribute_points()
    character.current_hp = character.hp

    character.print_stats()
    if confirm_your_choice():
        return character


def confirm_your_choice():
    confirmation = check_input('Are you happy with your character? Yes/no ',
                               ['Yes', 'No', 'Y', 'N'])
    if confirmation == 'No':
        print_and_pause('Let\'s do it again then')
        create_character()
    elif confirmation == 'Yes':
        return True
