# Write a class to hold player information, e.g. what room they are in
# currently.
# pylint: disable=C0321

class Player:
    def __init__(self, name, location):
        self.location = location
        self.name = name
        self.inventory = []

    # def add_item(self, Item):
    #     self.items.append(Item)
    
    def __str__(self):
        return f'{self.name} is in {self.location.name}'