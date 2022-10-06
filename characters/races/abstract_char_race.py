from abc import ABC, abstractmethod


class AbstractCharRace(ABC):

    @abstractmethod
    def __init__(self, character):
        self.character = character

    def set_race_bonuses(self,
                         bonus_strength=0,
                         bonus_agility=0,
                         bonus_cunning=0):

        self.character.strength += bonus_strength
        self.character.agility += bonus_agility
        self.character.cunning += bonus_cunning
