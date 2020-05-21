from room import *
from player import Player
from items import *
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

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Item Seeds
sword = Sword('sword', 'A very sharp blade.')
coins = Coins('coins', 'An amount to raise a family on.')
room['outside'].items = [sword]
room['treasure'].items = [coins]

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

movement = ('n', 's', 'e', 'w', 'drop', 'take', 'show')
direction_error = "There is no path in that direction, traveler."

while True:
    wrapper = textwrap.TextWrapper(width=80)
    print(f'\nPlayer {player_one.name} is in {player_one.room.name}.')
    print(f'They have the following items: {[x.name for x in player_one.items]}')
    # print(wrapper.wrap(player_one.room.description), '\n')
    command = input('Enter a command [n,s,e,w] to move\n[show] to see items in the room\n[take] to grab item from room\n[drop] to drop your item in the room\n[q to quit]: ').lower().split(' ')
    if command[0] == 'q':
        clearScreen()
        break
    if command[0] not in movement:
        print('Move is not allowed.')
    elif command[0] == 'n':
        if player_one.room.n_to is not None:
            player_one.room = player_one.room.n_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print(direction_error)
    elif command[0] == 'e':
        if player_one.room.e_to is not None:
            player_one.room = player_one.room.e_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print(direction_error)
    elif command[0] == 'w':
        if player_one.room.w_to is not None:
            player_one.room = player_one.room.w_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print(direction_error)
    elif command[0] == 's':
        if player_one.room.s_to is not None:
            player_one.room = player_one.room.s_to
            print(f"You've entered the {player_one.room.name}.")
            print(f'{player_one.room.description}')
        else:
            print(direction_error)
    elif command[0] == 'show':
        print(f"{player_one.room.name}'s items:")
        player_one.room.show_items()
    elif command[0] == 'take':
        try:
            for item_name in player_one.room.items:
                if command[1] == item_name.name:
                    player_one.get_item(item_name)
                    player_one.room.drop_item(item_name)
        except:
            print('There are no items to take.')
    elif command[0] == 'drop':
        try:
            for item_name in player_one.items:
                if command[1] == item_name.name:
                    player_one.drop_item(item_name)
                    player_one.room.add_item(item_name)
        except:
            print(f"{player_one.name} doesn't have any items.")