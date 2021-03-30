from abc import ABC, abstractmethod


class Instrument(ABC):

    @abstractmethod
    def play(self):
        pass


class Guitar(Instrument):
    def play(self):
        print("playing the guitar")


class Piano(Instrument):
    def play(self):
        print("playing the piano")


def play_instrument(instrument: Instrument):
    return instrument.play()


guitar = Guitar()
play_instrument(guitar)

piano = Piano()
play_instrument(piano)
