from characters.races.npc_races import Rat
from characters.races.playable_races import Human, Elf, Orc


def races_dict(race):

    races_data = {
        'Human': Human,
        'Elf': Elf,
        'Orc': Orc,
        'Rat': Rat
    }

    return races_data[race]
