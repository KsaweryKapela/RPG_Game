from characters.classes.playable_classes import Warrior, Rogue, Bard


def classes_dict(class_):
    classes_data = {
            'Warrior': Warrior,
            'Rogue': Rogue,
            'Bard': Bard
        }
    return classes_data[class_]