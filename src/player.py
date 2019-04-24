# Write a class to hold player information, e.g. what room they are in
# currently.
# pylint: disable=C0321

class Player:
    def __init__(self, location):
        self.location = location
        self.items = []

    def add_item(self, Item):
        self.items.append(Item)
    