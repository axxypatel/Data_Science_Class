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
current_step = 0           # variable to store the value of current step which player will take during the game.
player_health = 16         # player health variable at the start of game.

# All user defined function written below


def handle_input(user_input_temp):       # Function to handle the Input which checks the quality of the Input
    proper_input = True
    standard_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if user_input_temp not in standard_inputs:
        print("Your input is not available in the options provided earlier.")
        proper_input = False
        return proper_input

    return proper_input


def get_input(current_step_temp):          # Function to get the Input options for the player for each states comes during the game
    selected_option = 0
    user_options = {0: [],
                    1: [],
                    2: [],
                    3: [],
                    4: [],
                    5: []}
    stage_option = user_options[current_step_temp]
    print("Your option are mention below: \n", stage_option)
    user_input = int(input("Please enter your option"))
    check_input = handle_input(user_input)

    while not check_input:
        print("Your option are mention below: \n", stage_option)
        user_input = input("Please enter your option")
        check_input = handle_input(user_input)

    user_input_string = stage_option[user_input-1]
    track_player_step(user_input_string)
    global player_health
    player_health -= 1
    return user_input


def track_player_step(user_input_string_temp):  # Function to save all the steps which player will take during the game.
    global all_steps
    all_steps.append(user_input_string_temp)


# main code start from here


while player_health <= 0:  # main loop to check the lifeline of the player during the game
    next_input = get_input(current_step)



