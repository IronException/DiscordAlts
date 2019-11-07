import json


class Player:

    def __init__(self, json):
        pass

    # contains allvariables

    def add_self(self, depo):
        depo[self.name] = depo


def load_data():
    name_depo = {}
    print("loafing")
    pl = Player
    pl.add_self(name_depo)


def get_data(name):
    # somehow search the db now...
    return name_depo[name]
