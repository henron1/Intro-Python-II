# Implement a class to hold room information. This should have name and
# description attributes.
# pylint: disable=C0321

class Room:
    def __init__(self, name, description):
        # self.location = location
        self.description = description
        self.name = name
        self.items = []

    def print_items(self, Item):
        return print(f"{self.name: self.description}")

    def add_item(self, Item):
        print(f"You picked up a {self.items}")
