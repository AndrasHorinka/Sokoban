import game


def movement(table, direction):
    """ Checks if the user can move in the given direction, and returns the new map
    with updated positions of gamefield (incl. boxes, palyer.
    Arguments:
        table: type: list in list; the current game_map
        direction: type: string: wasd - defining in which direction we want to go/push

    Returns:
        updated_map: list in list, with  """

    current_map = table

    player_coordinates = search_position_in_table(current_map, "O")
    player_row = int(player_coordinates[0][0])
    player_col = int(player_coordinates[0][1])

    if direction in "wW":
        player_plus_1 = [player_row - 1, player_col]
        try:
            player_plus_2 = [player_row - 2, player_col]
        except IndexError:
            player_plus_2 = [[player_row - 1, player_col]]
    elif direction in "sS":
        player_plus_1 = [player_row + 1, player_col]
        try:
            player_plus_2 = [player_row + 2, player_col]
        except IndexError:
            player_plus_2 = [[player_row + 1, player_col]]
    elif direction in "aA":
        player_plus_1 = [player_row, player_col - 1]
        try:
            player_plus_2 = [player_row, player_col - 2]
        except IndexError:
            player_plus_2 = [[player_row, player_col] - 1]
    elif direction in "dD":
        player_plus_1 = [player_row, player_col + 1]
        try:
            player_plus_2 = [player_row, player_col + 2]
        except IndexError:
            player_plus_2 = [[player_row, player_col] + 1] 
    else:
        raise UserWarning("Incorrect movement")

    item_in_direction1 = current_map[player_plus_1[0]][player_plus_1[1]]
    item_in_direction2 = current_map[player_plus_2[0]][player_plus_2[1]]

    if item_in_direction1 in "B":
        if item_in_direction2 not in "BX":
            current_map[player_plus_2[0]][player_plus_2[1]] = "B"
            current_map[player_plus_1[0]][player_plus_1[1]] = "O"
            current_map[player_row][player_col] = "_"
    elif item_in_direction1 in "_S":
            current_map[player_plus_1[0]][player_plus_1[1]] = current_map[player_row][player_col]
            current_map[player_row][player_col] = "_"
    
    return current_map


def search_position_in_table(table, char_to_search):
    """ Search the coordinates of given character(s) in the table.
    Arguments:
        table: type - list (in list) of the current map
        char_to_search: type - string, Box, O character, etc.
    Returns:
        list: with coordinates """
    coordinates = []
    for rowind, row in enumerate(table):
        for charind, char in enumerate(row):
            if char == char_to_search:
                coordinates.append([rowind, charind])

    return coordinates
