from abc import ABC, abstractmethod


class AbstractCharClass(ABC):

    @abstractmethod
    def __init__(self, character):
        self.character = character

    @abstractmethod
    def give_starting_items(self):
        pass
