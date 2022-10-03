import time
from functions.rolls import k100
import os


def print_and_pause(string, pause_time=1):
    print(string)
    time.sleep(pause_time)


def print_and_pause_multiple(string, pause_time=1):
    text = string.split('\n')
    for line in text:
        print_and_pause(line, pause_time)


def check_input(string, list_of_answers=False):
    if str(string)[-1] != ' ':
        string = str(string) + ' '
    answer = input(string).capitalize()
    if answer == 'Help':
        print(list_of_answers)
        return check_input(string, list_of_answers)

    if list_of_answers:
        if answer not in list_of_answers:
            print('Invalid response')
            return check_input(string, list_of_answers)
    return answer.capitalize()


def check_input_multiple(string, list_of_answers=False):
    new_string = string.split('\n')
    for line in new_string:

        if line == new_string[-1]:
            answer = input(line).capitalize()
            if answer not in list_of_answers:
                print_and_pause('Invalid response')
                return check_input(line, list_of_answers)
            else:
                return answer.capitalize()

        else:
            print_and_pause(line)

    raise 'Last line != last loop iteration!!!'


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


def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_text(file_path):
    with open(file_path) as f:
        for line in f:
            print_and_pause(line.strip())
    time.sleep(2)
