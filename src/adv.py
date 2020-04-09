from room import Room
from player import Player
import textwrap

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


# # Link rooms together

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

player_name = input('Enter your name: ')
player_one = Player(player_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def clearScreen():
    number = 80
    while number > 0:
        print("")
        number -= 1
    return

movement = ('n', 's', 'e', 'w')

while True:
    # clearScreen()
    wrapper = textwrap.TextWrapper(width=80)
    print(f'\nPlayer {player_one.name} is in {player_one.room.name}.')
    print(wrapper.wrap(player_one.room.description))
    direction = input('Please choose a direction [n,s,e,w] q to quit: ').lower()
    if direction.lower() == 'q':
        clearScreen()
        break
    if direction not in movement:
        print('Move is not allowed.')
    elif direction == 'n':
        if player_one.room.n_to is not None:
            player_one.room = player_one.room.n_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print("There is no path in that direction, traveler.")
    elif direction == 'e':
        if player_one.room.e_to is not None:
            player_one.room = player_one.room.e_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print("There is no path in that direction, traveler.")
    elif direction == 'w':
        if player_one.room.w_to is not None:
            player_one.room = player_one.room.w_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print("There is no path in that direction, traveler.")
    elif direction == 's':
        if player_one.room.s_to is not None:
            player_one.room = player_one.room.s_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print("There is no path in that direction, traveler.")