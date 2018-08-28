import game

def movement(direction):
    """ Checks if the user can move in the given direction, and returns the new map
    with updated positions of gamefield (incl. boxes, palyer.
    Arguments:
        direction: wasd - defining in which direction we want to go/push
    
    Returns: 
        updated_map: list in list, with  """
    
    # 1. read the whole game_map
    # 2. define player position
    # 3. check what is in direction
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



