from abc import ABC, abstractmethod


class Instrument(ABC):

    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"playing the {self.name}")


class Piano(Instrument):

    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"playing the {self.name}")


def play_instrument(instrument: Instrument):
    return instrument.play()


guitar = Guitar("Guitar")
play_instrument(guitar)

piano = Piano("Piano")
play_instrument(piano)
