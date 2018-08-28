def show_menu(title, menu_elements, quit):
    """ Prints the menu to the screen.
    Args:
        title (str): menu title
        menu_elements (list): list of strings - options that will be shown in menu
        quit (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console."""
    print("\n")
    print("\033[1;33m" + title + "\033[00m")
    for i in range(len(menu_elements)):
        print("\t ({0}) {1}".format((i + 1), menu_elements[i]))
    print("\t (0) {0}".format(quit))


def get_input(input_questions):
    """ Ask the questions and return the answers as a list.

    Arguments: questions in a list

    Returns: answers in a list """
    answers = []
    for question in input_questions:
        answers.append(input("{0}: ".format(question)))
    return answers


def print_table(table, score):
    """ Prints a table with a header, where header may contain Steps, Pushes, Tries, etc.

    Arguments:
        table: type: list in list, containing the map of Sokoban
        score: type: dictionary with score:value containing the Steps, Pushes
        """
    # 1. check length of game_map
    map_length = 2 * len(table[0]) - 1

    # 2. check length dictionary
    key_length  = len(list(score.keys())) + 1
    for key in list(score.keys()):
        key_length += len(key)
    
    for dict_value in list(score.values())):
        key_length += len(str(dict_value))
     
    # 3. compare and give back longest entry
    if map_length > key_length:
        max_length = map_length
    else:
        max_length = key_length
        # map_length += (key_length - map_length) // 2  
    
    # 4. print header based on max_length
    print("\n" + "\033[1;96m" + "{0:^{width}}" + "\033[00m".format(score.items(), width=int(max_length -key_length)))

    # 5. print map - but if its 
    #         a wall --> color as dark gray back "\033[1;96m"
    #         player --> color as light blue back  "\033[1;104m"
    #         box --> color as light green back --> "\033[1;103m"
    #         winzone --> color as light yellow back --> "\033[1;102m"
    #         free space --> white background --> "\033[1;107m"
    for row in table:
        for char in row:
            if char == X:
                print("\033[1;100m" + "X" + "\033[00m", end="")
            elif char == "O":
                print("\033[1;104m" + "O" + "\033[00m", end="")
            elif char == "S":
                print("\033[1;102m" + "O" + "\033[00m", end="")
            elif char == "B":
                print("\033[1;103m" + "O" + "\033[00m", end="")
            elif char == "_":
                print("\033[1;107m" + " " + "\033[00m", end="")








    # print the title of the table
    for i in range(len(score)):  # iterate per lines columns
        print(
            "\033[1;96m" + "|" + "\033[00m" + "\033[1;33m" + "{0:^{width}}".format(
                score[i],
                width=int(
                    column_width[i])) + "\033[00m",
            end="")
    print("\033[1;96m" + "|" + "\033[00m")

    # print the list elements
    for n in range(len(table)):  # iterate per lines
        for m in range(len(score)):  # iterate per columns
            print(
                "\033[1;96m" + "|" + "\033[00m" + "{0:^{width}}".format(
                    table[n][m],
                    width=int(
                        column_width[m])),
                end="")
        print("\033[1;96m" + "|" + "\033[00m")

    print("\033[1;96m" + "\\" + "-" * (maxwidth + len(score) - 1) + "/" + "\033[00m")


def print_error_message(err):
    print(err)