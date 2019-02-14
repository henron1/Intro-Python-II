# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, location, description):
        self.location = location
        self.description = description
        self.items = []

    def __str__(self):
        return f"{self.location}\n{self.description}\n\n"


