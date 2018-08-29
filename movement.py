import game


def movement(table, direction):
    """ Checks if the user can move in the given direction, and returns the new map
    with updated positions of gamefield (incl. boxes, palyer.
    Arguments:
        table: type: list in list; the current game_map
        direction: type: string: wasd - defining in which direction we want to go/push

    Returns:
        updated_map: list in list, with  """

    # 1. read the whole game_map
    current_map = table

    # 2. define player position
    player_coordinates = search_position_in_table(current_map, "X")
    player_row = int(player_coordinates[0])
    player_col = int(player_coordinates[1])

    # 3. check what is in direction
    if direction == "W":
        item_in_direction1 = search_item_in_table_position(current_map, player_row - 1, player_col)
        try:
            item_in_direction2 = search_item_in_table_position(current_map, player_row - 2, player_col)
        except IndexError:
            item_in_direction2 = "X"
    elif direction == "S":
        item_in_direction1 = search_item_in_table_position(current_map, player_row + 1, player_col)
        try:
            item_in_direction2 = search_item_in_table_position(current_map, player_row + 2, player_col)
        except IndexError:
            item_in_direction2 = "X"

    if direction == "A":
        item_in_direction1 = search_item_in_table_position(current_map, player_row, player_col - 1)
        try:
            item_in_direction2 = search_item_in_table_position(current_map, player_row, player_col - 2)
        except IndexError:
            item_in_direction2 = "X"
    elif direction == "D":
        item_in_direction1 = search_item_in_table_position(current_map, player_row, player_col + 1)
        try:
            item_in_direction2 = search_item_in_table_position(current_map, player_row, player_col + 2)
        except IndexError:
            item_in_direction2 = "X"

    #     if nothing, just move player
    #     else: check
    #         what is in direction +1
    #             if wall --> block, cannot move
    #             else:
    #                 check if what is in direction +2:
    #                 if not whitespace (_) --> block
    #                 else: 
    #                     move player in direction +1
    #                     move box in direction +1

    # 4. update the game_map
    # 5. call game.check_win_condition
    # 6. return game_map

    pass
    # Andras


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


def search_item_in_table_position(table, row, col):
    """ Search what is in the given in the table.
    Arguments:
        table: type - list (in list) of the current map
        row: type - integer; the coordinate of row
        col: type - integer; the coordinate of column
    Returns:
        Item Char: type: string (X, O, B, S) """
    item_char = ""
