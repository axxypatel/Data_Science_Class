# Advanture Trip Text Game

print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("Game Start")
print("------------------------------------------------------------")
print("------------------------------------------------------------")
print("Hello and welcome to the Adventure Trip Game.")
print("This is a text based game where you have to 17select options on every state.")
print("Game Rules: You have to collect things from the different rooms/kitchen/living room of house which are extremly(Focus on this word :D) necessary for the adventure trip.")
print("Winning condition of the game is depend on the number of items which you select during game. If you collected all the necessary items then you are ready to go on adventure trip.")
print("You should collect all the items within 16 or less steps in order to win the game.")
print("Objective: Collect all the necessary items that are needed to go on adventure trip.")

all_steps = ["Start of a Game and you are standing in Lobby of House"]  # This list will store all the steps of the player
player_steps = 16         # player health variable at the start of game.

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
    user_options = {0: ["You are currently in - The Lobby", "[1] - Go to the Living Room", "[2] - Go to Room 1", "[3] - Stay here and cancel the trip", "[4] - Get hiking shoes from box and put them on", "[5] - Pick up the crocs"],
                    1: ["You are currently in - The Living Room", "[1] - Go back to the Lobby", "[2] - Go to Room 1", "[3] - Take the bag", "[4] - Pick up car keys", "[5] - Pick up the deodorant"],
                    2: ["You are currently in - Room 1 (Clothes)", "[1] - Go to Lobby", "[2] - Go to Living Room", "[3] - Go to Room 2", "[4] - Get clothes from closet", "[5] - Pick up iPod", "[6] - Pick up charger"],
                    3: ["You are currently in - Room 2 (Safety Items)", "[1] - Go back to the Room 1", "[2] - Go to Room 3", "[3] - Take torch, pair of batteries, first aid kit and Map", "[4] - Pick up anti-glare sunglasses", "[5] - Pick up the axe"],
                    4: ["You are currently in - Room 3 (Tent)", "[1] - Go back to the Room 2", "[2] - Go to the kitchen", "[3] - Take the tent", "[4] - Take the sleeping bag", "[5] - Take the travel pillow", "[6] - Take the comforter"],
                    5: ["You are currently in - The Kitchen", "[1] - Take the bread packet", "[2] - Take extra protein bars", "[3] - Go back to Room 2", "[4] - Go back to the Room 3", "[5] - Finish packing and go back to the Lobby"]}


    stage_option = user_options[current_step_temp]
    print("********************************************************************************")
    print("********************************************************************************")
    print("Your options are mentioned below: \n", *stage_option, sep="\n")   # This will display all the option in new line
    user_input = input("Please enter your option:\n")
    check_input = handle_input(user_input)

    while not check_input:
        print("Your options are mentioned below: \n", *stage_option, sep="\n")
        user_input = input("Please enter your option:\n")
        check_input = handle_input(user_input)

    user_input = int(user_input)
    user_input_string = stage_option[user_input]
    track_player_step(user_input_string)
    global player_steps
    player_steps -= 1
    return user_input


def track_player_step(user_input_string_temp):  # Function to save all the steps which player will take during the game.
    global all_steps
    all_steps.append(user_input_string_temp)


def winning_condition_check():
    win_condition = {"[3] - Take the bag", "[4] - Get clothes from closet", "[3] - Take torch, pair of batteries, first aid kit and Map", "[3] - Take the tent", "[4] - Take the sleeping bag", "[2] - Take extra protein bars", "[4] - Get hiking shoes from box and put them on"}
    match_steps = win_condition.intersection(set(all_steps))
    if len(match_steps) == 7:
        return True
    else:
        return False


def show_player_steps():
    print("********************************************************************************")
    print("********************************************************************************")
    print("Please type YES/NO if you want to check all the steps taken during game.")
    show_step_input = input()
    if show_step_input.upper() == "YES":
        print("*************************Steps Report******************************************")
        print(*all_steps, sep='\n')
        print("*************************Player Steps******************************************")
        print("Remaining steps :", player_steps)
    else:
        print("Hope you enjoyed the game")


next_input = 0            # variable to store the next input which user has entered from the choices
current_step = 0          # variable to store the value of current step which player will take during the game.
while player_steps > 0:  # main loop to check the lifeline of the player during the game
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
        print("You have collected all the items needed for trip. Go ahead and enjoy!")
        print("----------------------------")
        show_player_steps()
        break
else:
    print("********************************************************************************")
    print("********************************************************************************")
    print("********************************************************************************")
    print("You have used up all your steps.")
    show_player_steps()
    print("Game over")
