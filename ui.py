def showmenu(title, menu_elements, quit):
    """ Prints the menu to the screen.
    Arguments: 
        Title: title of the menu
        menu_elements: the options of the menu in a list
        quit: quit message 
    
    Returns:
        Nothing, it just prints"""
    
    


def get_input(input_questions):
    """ Ask the questions and return the answers as a list.

    Arguments: questions in a list

    Returns: answers in a list """
    answers = []
    for question in input_questions:
        answer = input(question)
        answers.append(answer)
    return answers

