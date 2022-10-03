from functions.basic_functions import print_and_pause


class CheckInput:
    def __init__(self, character):
        self.character = character
        self.basic_commands = ['Stats', 'Eq', 'Help']
        self.commands_dictionary = {'Stats': self.character.print_stats,
                                    'Eq': self.character.eq.print_eq,
                                    'Help': self.help}

        self.current_list_of_answers = None
        self.current_input_string = None

    def catch_input(self, string, list_of_answers=False):
        if str(string)[-1] != ' ':
            self.current_input_string = str(string) + ' '
        else:
            self.current_input_string = string

        self.current_list_of_answers = list_of_answers
        return self.check_input()

    def check_input(self):

        answer = input(self.current_input_string).capitalize()
        if answer in self.basic_commands:
            self.commands_dictionary[answer]()
            return self.check_input()

        if self.current_list_of_answers:
            if answer not in self.current_list_of_answers:
                print('Invalid response')
                return self.check_input()

        return answer.capitalize()

    def help(self):
        print(f'Situational commands: {self.current_list_of_answers}')
        print(f'Basic commands: {self.basic_commands}')
