# main game methods
import file_manager
import ui
import movement


def start_module(game_map):
    """ Loads the selected map (default if none given)
    Arguments: 
        game_map: a list in list with the selected map
    Returns:
        None, it just prints the map """
    win_cords = define_coords_of_win_condition(game_map)
    score_list = {"Steps": 0, "Push": 0}
    actual_map = game_map
    while True:
        ui.print_table(actual_map, score_list)
        try:
            next_move = ui.get_input(["Make your move!, Q for exit"])
            choice = next_move[0]
            if choice == "q":
                return False
            actual_map = movement.movement(actual_map, str(choice))

        except KeyError as err:
            print("There is no such option! Use WASD to move or Q to quit!")


def define_coords_of_win_condition(game_map):
    """ Define the zones of win condition (winzones);
    Argument: 

    game_map: list in list of the original game map

    Returns: tuple/list of the coordinates of the winzones
     """
    # Geri

    pass


def define_current_position(game_map):
    """ Define the position of the Player in given map
    Arguments:
        table: list in list - current map
        
    Return: 
        coordinates of player as list [y, x] where y is the first list coordinate, x is the list in list coordinate  """
    
    pass
    # Geri 


def check_win_condition(game_map, win_zones):
    # 1. read the game_map
    # 2. crosscheck if coordinates of boxes in table == to win_zones coordinates
    #       if yes --> return win --
    # 3. sys.exit() --> step back 3 stacks

    pass
    # Geri


def select_level():
    pass


def save_game():
    pass


def load_game():
    pass
