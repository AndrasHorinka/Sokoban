# main game methods
import file_manager
import ui
import movement
import start
# import sys


def start_module(game_map):
    """ Loads the selected map (default if none given)
    Arguments: 
        game_map: a list in list with the selected map
    Returns:
        None, it just prints the map """
    win_zones = define_coords_of_searched_letter(game_map, "S")
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
    """ Define the zones of win condition (winzones);
    Argument: 

    game_map: list in list of the original game map

    Returns: tuple/list of the coordinates of the winzones
     """
    win_zones = []
    for pos, line in enumerate(game_map):
        for char, row in enumerate(line):
            if letter == row:
                win_zones.append([pos, char])
    return win_zones


def check_win_condition(game_map, win_zones):
    current_map = game_map
    for zone in win_zones:
        if current_map[zone[0]][zone[1]] not in "B":
            return True
        else:
            continue
    ui.print_table(current_map, {})
    print("You Win!!")
    start.os.sys.exit(0)


def select_level():
    pass


def save_game():
    pass


def load_game():
    pass
