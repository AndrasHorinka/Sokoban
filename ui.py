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
    header = ""
    for key in list(score.keys()):
        header += str(key) + " " + str(score.get(key)) + " "

    # 4. print header based on max_length
    print("\t" "\033[1;96m" + "{0:<}".format(header) + "\033[00m")

    for row in table:
        print("\t", end="")
        for char in row:
            if char == "X":
                print("\033[1;48m" + "X" + "\033[00m", end="")
            elif char == "O":
                print("\033[1;41m" + "O" + "\033[00m", end="")
            elif char == "S":
                print("\033[1;103m" + "S" + "\033[00m", end="")
            elif char == "B":
                print("\033[1;42m" + "B" + "\033[00m", end="")
            elif char == "_":
                print(" ", end="")
            else:
                raise ImportWarning("Unidentified character in map!")
        print("")


def print_error_message(err):
    pass
