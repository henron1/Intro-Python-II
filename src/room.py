# Implement a class to hold room information. This should have name and
# description attributes.
# pylint: disable=C0321

class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.items = []

    def print_items(self, Item):
        return print(f"{Item.name: Item.description}")

    def add_item(self, Item):
        self.items.append(Item)