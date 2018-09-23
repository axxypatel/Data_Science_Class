# Advanture Trip Text Game

print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("Game Start")
print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("Put Description of the advanture Trip Text Game")
print("Print rule and condition for the game")
print("Print winning condition for the game")
print("Print the health of the player")

all_steps = ["Start of a Game and you are standing in Lobby of House"]           # This list will store all the steps of the player
player_health = 16         # player health variable at the start of game.

# All user defined function written below


def handle_input(user_input_temp):       # Function to handle the Input which checks the quality of the Input
    proper_input = True
    standard_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if user_input_temp.isnumeric():
        user_input_temp = int(user_input_temp)
        if user_input_temp not in standard_inputs:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("Your input is not available in the options provided earlier. Please choose option again.")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            proper_input = False
    else:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Your input is not number. Please choose option again.")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        proper_input = False
    return proper_input


def get_input(current_step_temp):          # Function to get the Input options for the player for each states comes during the game
    # All option of various stages are stored below dictonary
    user_options = {0: ["Hint - Lobby of the House", "[1] - Go to the Living Room", "[2] - Go to the Room1", "[3] - Stay here and cancel the Adventurous trip with friends"],
                    1: ["Living Room", "[1] - Go back to the Lobby", "[2] - Go to Room1", "[3] - Take the bag", "[4] - Grab the grooming stuff", "[5] - Don't forget to take the deodorant"],
                    2: ["Room 1 (Clothes)", "[1] - Go to Lobby", "[2] - Go to Living Room", "[3] - Go to Room 2", "[4] - Open the cupboard and take clothes", "[5] - Open the box wear the shoes and get Ready", "[6] - Take the iPod", "[7] - Take the charger"],
                    3: ["Room 2 (Safety Things)", "[1] - Go back to the Room1", "[2] - Go to Room 3", "[3] - Take torch, pair of batteries,  first aid kit and Map"],
                    4: ["Room 3 (Tent)", "[1] - Go back to the room 2", "[2] - Go to kitchen", "[3] - Take the tent", "[4] - Take the Sleeping bag", "[5] - Take the travel pillow", "[6] - take the comforter"],
                    5: ["Kitchen", "[1] - Pack the required food", "[2] - Take the protein bars", "[3] - Take the water bottles", "[4] - Go back to the Room 3", "[5] - If you're done picking things go back to the Lobby"]}

    stage_option = user_options[current_step_temp]
    print("********************************************************************************")
    print("********************************************************************************")
    print("Your option are mention below: \n", *stage_option, sep="\n")   # This will display all the option in new line
    user_input = input("Please enter your option:\n")
    check_input = handle_input(user_input)

    while not check_input:
        print("Your option are mention below: \n", *stage_option, sep="\n")
        user_input = input("Please enter your option:\n")
        check_input = handle_input(user_input)

    user_input = int(user_input)
    user_input_string = stage_option[user_input]
    track_player_step(user_input_string)
    global player_health
    player_health -= 1
    return user_input


def track_player_step(user_input_string_temp):  # Function to save all the steps which player will take during the game.
    global all_steps
    all_steps.append(user_input_string_temp)


def winning_condition_check():
    win_condition = {"[3] - Take the bag", "[4] - Open the cupboard and take clothes", "[3] - Take torch, pair of batteries,  first aid kit and Map", "[3] - Take the tent", "[4] - Take the Sleeping bag", "[2] - Take the protein bars"}
    match_steps = win_condition.intersection(set(all_steps))
    if len(match_steps) == 6:
        return True
    else:
        return False


def show_player_steps():
    print("********************************************************************************")
    print("********************************************************************************")
    print("Please type YES/NO if you want to check all the steps taken during game.")
    show_step_input = input()
    if show_step_input.upper() == "YES":
        print("*************************Health Report******************************************")
        print(*all_steps, sep='\n')
        print("*************************Player Health******************************************")
        print("Your health remaining in the game is :", player_health)
    else:
        print("Hope you enjoyed the game")


next_input = 0            # variable to store the next input which user has entered from the choices
current_step = 0          # variable to store the value of current step which player will take during the game.
while player_health > 0:  # main loop to check the lifeline of the player during the game
    if current_step == 0:
        next_input = get_input(current_step)
        if next_input == 1:
            current_step = 1
        elif next_input == 2:
            current_step = 2
        elif next_input == 3:
            break

    elif current_step == 1:
        next_input = get_input(current_step)
        if next_input == 1:
            current_step = 0
        elif next_input == 2:
            current_step = 2

    elif current_step == 2:
        next_input = get_input(current_step)
        if next_input == 1:
            current_step = 0
        elif next_input == 2:
            current_step = 2
        elif next_input == 3:
            current_step = 3

    elif current_step == 3:
        next_input = get_input(current_step)
        if next_input == 1:
            current_step = 2
        elif next_input == 2:
            current_step = 4

    elif current_step == 4:
        next_input = get_input(current_step)
        if next_input == 1:
            current_step = 3
        elif next_input == 2:
            current_step = 5

    elif current_step == 5:
        next_input = get_input(current_step)
        if next_input == 4:
            current_step = 4
    if winning_condition_check():
        print("********************************************************************************")
        print("********************************************************************************")
        print("********************************************************************************")
        print("You collected all the items needed for trip. Go ahead and enjoy the trip")
        print("----------------------------")
        show_player_steps()
        break
else:
    print("********************************************************************************")
    print("********************************************************************************")
    print("********************************************************************************")
    print("You are not left with any health.")
    show_player_steps()
    print("Game over")
