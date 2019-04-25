# pylint: disable=C0321
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Henry", room['outside'])
# print(player)


# def item_prompt():
#     prompt = input("What would you like to do with this item?")


optional_directions ="Go n, s, e, w!"

#################################### Game LOOP ####################################

while True:
    # * Prints the current room name        
    print(f"{player.name} is in {player.location.name}")

    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    travel = input("Please enter a direction for your player to travel to:\n").lower()[0]
    # print(travel)
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    if travel == 'n' and player.location.name != 'overlook' and player.location.name != 'treasure':
        player.location = player.location.n_to
    elif travel == 's' and player.location.name != 'narrow' and player.location.name != 'outside':
        player.location = player.location.s_to
    elif travel == 'e' and player.location.name != 'narrow' and player.location.name != 'treasure' and player.location.name != 'overlook' and player.location.name != 'outside':
        player.location = player.location.e_to
    elif travel == 'w':
        player.location = player.location.w_to
    elif travel == 'q':
        print("Game Over!")
    else:
        print("please enter either n, s, e, w")