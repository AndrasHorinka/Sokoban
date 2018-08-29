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