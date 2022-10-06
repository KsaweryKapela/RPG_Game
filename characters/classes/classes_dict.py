from characters.classes.playable_classes import Warrior, Rogue, Bard


def classes_dict(char_class):
    classes_data = {
            'Warrior': Warrior,
            'Rogue': Rogue,
            'Bard': Bard
        }
    return classes_data[char_class]
