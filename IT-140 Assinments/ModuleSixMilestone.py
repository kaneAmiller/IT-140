# Kane Miller

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
start_room = 'Great Hall'  # Starting room
end_room = 'Cellar'  # Room you end at (fight the boss)
# A dictionary for the directions
directions = {'north': 'North', 'south': 'South', 'east': 'East', 'west': 'West',
              'go north': 'North', 'go south': 'South', 'go east': 'East', 'go west': 'West'}
command = ''  # input
current_room = start_room
instructions = 'write instructions here'


def current_status(current_room, end_room):  # displays player status and possible moves
    print('You are in the', current_room)
    if current_room == end_room:
        print('Congrats, you finished the game!')
        return True
    else:
        directions_list = list(rooms[current_room].keys())
        if len(directions_list) == 2:
            print('You can go', ', or '.join(directions_list))
        elif len(directions_list) == 3:
            print('You can go', ', , or '.join(directions_list))
        elif len(directions_list) == 4:
            print('You can go', ', , , or '.join(directions_list))
        else:
            print('You can go', ''.join(directions_list))
        return False


# This function takes the dictionary of rooms, the user's input 'move', and the current room name.
# if move (the key for rooms) is valid the new room will be assigned, if not: "You can't go that way." gets printed
def move_between_rooms(rooms, move, current_room):
    new_room = rooms[current_room].get(directions.get(move))
    if new_room:
        return new_room
    else:
        print("You can't go that way.")
        return current_room


current_status(current_room, end_room)  # Print the starting room

while command.lower() != 'exit':
    command = input()
    if command.lower() == 'exit':
        break # Exit the game loop
    elif command.lower() in directions:
        current_room = move_between_rooms(rooms, command.lower(), current_room)
        if current_status(current_room, end_room):
            break  # Exit the game loop
    else:
        print("Invalid command.")
