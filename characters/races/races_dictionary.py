from characters.races.npc_races import Rat, Bear, Raccoon, Hedgehog
from characters.races.playable_races import Human, Elf, Orc


def races_dict(race):

    races_data = {
        'Human': Human,
        'Elf': Elf,
        'Orc': Orc,
        'Rat': Rat,
        'Bear': Bear,
        'Raccoon': Raccoon,
        'Hedgehog': Hedgehog
    }

    return races_data[race]
