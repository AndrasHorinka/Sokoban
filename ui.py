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
        table: type: list, containing the map of Sokoban
        score: type: list containing the Steps, Pushes, Tries, etc. or anything else as per the list elements
        """
    # check what is the longest entry per column - and feed it into a list (+4
    # to have some spaces)
    column_width = []
    for i in range(len(title_list)):
        length = len(title_list[i])
        for n in range(len(table)):
            if len(table[n][i]) > length:
                length = len(table[n][i])
        column_width.append(length + 4)

    # print the header of the table based on above calculations:
    maxwidth = common.get_sum_of_list(column_width)
    print("\n" + "\033[1;96m" + "/" + "-" * (maxwidth + len(title_list) - 1) + "\\" + "\033[00m")

    # print the title of the table
    for i in range(len(title_list)):  # iterate per lines columns
        print(
            "\033[1;96m" + "|" + "\033[00m" + "\033[1;33m" + "{0:^{width}}".format(
                title_list[i],
                width=int(
                    column_width[i])) + "\033[00m",
            end="")
    print("\033[1;96m" + "|" + "\033[00m")

    # print the list elements
    for n in range(len(table)):  # iterate per lines
        for m in range(len(title_list)):  # iterate per columns
            print(
                "\033[1;96m" + "|" + "\033[00m" + "{0:^{width}}".format(
                    table[n][m],
                    width=int(
                        column_width[m])),
                end="")
        print("\033[1;96m" + "|" + "\033[00m")

    print("\033[1;96m" + "\\" + "-" * (maxwidth + len(title_list) - 1) + "/" + "\033[00m")