import time

from rolls import k100


def print_and_pause(string, pause_time=1):
    print(string)
    time.sleep(pause_time)


def is_lucky(entity_luck):
    roll = k100()

    if roll <= entity_luck:
        return True
    else:
        return False


def is_crit(entity_crit_chance):
    roll = k100()

    if roll <= entity_crit_chance:
        return True
    else:
        return False

