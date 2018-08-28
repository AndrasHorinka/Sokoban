import ui
import file_manager
import game
import os


def choose():
    inputs = ui.get_input(["Please enter a number: "], "")
    option = inputs[0]
    game_level = file_manager.get_table_from_file("map.csv")

    if option == "1":
        game.start_module(game_level)
    elif option == "2":
        game.select_level()
    elif option == "3":
        game.save_game()
    elif option == "4":
        game.load_game()
    elif option == "0":
        os.sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Play Game",
               "Choose level",
               "Save Game",
               "Load Saved Game",]

    ui.show_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()
