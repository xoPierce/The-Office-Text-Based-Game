# Jeffery Pierce Waren - Project 2

# A dictionary for The Office text game.
# The dictionary links a room to other rooms.
rooms = {
    'Michael\'s Office': {
        'South': 'West Sales Floor',
        'staff': []
    },
    'West Sales Floor': {
        'West': 'Reception',
        'East': 'East Sales Floor',
        'North': 'Michael\'s Office',
        'South': 'Accounting',
        'staff': ['Dwight', 'Jim']
    },
    'Reception': {
        'East': 'West Sales Floor',
        'staff': []
    },
    'Accounting': {
        'North': 'West Sales Floor',
        'staff': ['Oscar', 'Angela']
    },
    'East Sales Floor': {
        'West': 'West Sales Floor',
        'East': 'Kitchen',
        'North': 'Conference Room',
        'staff': ['Stanley', 'Phyllis']
    },
    'Conference Room': {
        'South': 'East Sales Floor',
        'staff': ['Creed']
    },
    'Kitchen': {
        'West': 'East Sales Floor',
        'East': 'Annex',
        'staff': ['Meredith']
    },
    'Annex': {
        'West': 'Kitchen',
        'North': 'Break Room',
        'staff': ['Ryan', 'Kelli', 'Toby']
    },
    'Break Room': {
        'South': 'Annex',
        'staff': ['Kevin']
    },
}

current_room = 'Michael\'s Office'
staff_list = []


def gameInstructions():
    # print a start menu and instructions for the game
    print("Welcome to The Office Adventure Game!\n")
    print("""
You are playing as Michael Scott, manager of Dunder Mifflin inc.
You must gather all of your staff before you are late to your team outing!
Don't forget any of your staff members or beware that your office morale may be at an all time low!
The Scranton branch may be at risk of getting downsized if sales don\'t go up!\n
    """)
    print("Move commands: go South, go North, go East, go West\n")
    print("Add to Inventory: get 'team member name'")
    print("Hint: There are 12 staff members that will need to be collected before you can leave the office. Good luck!")


def showStatus(current_pos, room_dict):
    # print the player's current status.
    print('-----------------------------------')
    print("Current room: {}".format(current_pos))
    print('Current staff collected: {}'.format(staff_list))
    if (len(room_dict[current_pos]['staff'])) > 0:
        print('You have found {}!'.format(room_dict[current_pos]['staff']))


def player_move(current_pos, room_dict):
    # function to get an input and move the player between rooms
    global current_room  # gets the global var, so it can be updated within the function
    showStatus(current_room, rooms)
    move = input('Enter your move: \n')
    move_tokens = move.split()
    if len(move_tokens) <= 1:  # prints invalid input if there is only 1 token
        print('Invalid input!')
        player_move(current_room, rooms)
    else:
        # checks each user input to respond appropriately. Ex (inv direction, inv input, or update current room.)
        if (any([
            move_tokens[1] == 'North', move_tokens[1] == 'South',
            move_tokens[1] == 'East', move_tokens[1] == 'West'
            and len(move_tokens) == 2 and move_tokens[0] == 'go'
        ])):
            direction = move_tokens[1]
            if direction in room_dict[current_room]:
                current_room = (room_dict[current_pos][direction])  # updates current room
            else:
                print('Invalid direction!')  # prints invalid direction if user inputs a direction they can't go
                player_move(current_room, room_dict)
        elif move_tokens[0] == 'get' and (len(room_dict[current_room]['staff'])) > 0:
            # elif statement to get different staff members and add them to a list
            if rooms[current_pos]['staff'].count(move_tokens[1]) == 1:
                staff_index = room_dict[current_pos]['staff'].index(move_tokens[1])
                staff_list.append(room_dict[current_pos]['staff'][staff_index])
                print('You have gathered {}!'.format(room_dict[current_pos]['staff'][staff_index]))
                room_dict[current_pos]['staff'].remove(move_tokens[1])
                player_move(current_room, rooms)
        else:
            print('Invalid input!')  # if all other statements are not true then print invalid input
            player_move(current_room, rooms)


def main():
    # main gameplay loop
    gameInstructions()
    # infinite loop
    while True:
        player_move(current_room, rooms)
        if current_room == 'Reception' and len(staff_list) == 12:       # Win game
            print("""Awesome job! Michael has successfully gathered everyone! I guess you could call him the World\'s
best boss. Getting a big boost in office moral from the outing will surely keep the Scranton branch from 
getting downsized!
            """)
            quit()
        elif current_room == 'Reception' and len(staff_list) != 12:     # Lose game
            print("""
Pam can\'t let you leave anyone behind! Looks like you\'re going to have to cancel the team outing!
Office moral will be at an all time low and Dunder Mifflin will risk being downsized or even shut down
completely! Game over!
            """)
            quit()


main()
