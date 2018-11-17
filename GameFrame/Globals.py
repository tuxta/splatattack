
class Globals:

    running = True
    FRAMES_PER_SECOND = 30

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    SCORE = 0

    # - Set the starting number of lives - #
    LIVES = 3

    # - Set the Window display name - #
    window_name = 'Splat Attack'

    # - Set the order of the rooms - #
    levels = ["Title", "PlayRoom1", "Score", "PlayRoom2", "Score", "PlayRoom3", "FinalScore"]

    # - Set the starting level - #
    start_level = 0

    # - Set this number to the level you want to jump to when the game ends - #
    end_game_level = 0

    # - This variable keeps track of the room that will follow the current room - #
    # - Change this value to move through rooms in a non-sequential manner - #
    next_level = 0
    
    # - Change variable to True to exit the program - #
    exiting = False


# ############################################################# #
# ###### User Defined Global Variables below this line ######## #
# ############################################################# #

    num_ants = 0
    num_spiders = 0
    num_scorpions = 0
    num_roaches = 0
