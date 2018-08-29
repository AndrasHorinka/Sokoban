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
    win_zones = define_coords_of_searched_letter(game_map,letter)
    score_list = {"Steps": 0, "Push": 0}
    actual_map = game_map
    while True:
        check_win_condition(actual_map, win_zones)
        ui.print_table(actual_map, score_list)
        next_move = ui.get_input(["Make your move!, Q for exit"])
        while next_move[0] not in "wWaAsSdDqQ":
            next_move = ui.get_input(["Make your move!, Q for exit"])
        if next_move[0] == "q":
            return False
        actual_map = movement.movement(actual_map, str(next_move[0]))



def define_coords_of_searched_letter(game_map,letter):
    win_zones = []
    for pos, line in enumerate(game_map):
        for char, row in enumaret(line):
            if letter == row:
                win_zones.append([pos, char])
    return win_zones

    """ Define the zones of win condition (winzones);
    Argument: 

    game_map: list in list of the original game map

    Returns: tuple/list of the coordinates of the winzones
     """
    

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
    current_map = game_map

    # 2. crosscheck if coordinates of boxes in table == to win_zones coordinates
    #       if yes --> return win --
    
    for win_zones in game_map[zone[0], zone[1]]:
        if win_zone not in "B":
            return False
        else:
            pass
    # (3. sys.exit() --> step back 3 stacks)
    print("You Win!!")
    sys.exit()

list[[0][1]]

def restart_game():
    pass


def select_level():
    pass


def save_game():
    pass


def load_game():
    pass
# main game methods  
