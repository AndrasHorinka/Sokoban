import ui
import file_manager


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        game.start_module()
    elif option == "2":
        game.select_level()
    elif option == "3":
        game.save_game()
    elif option == "4":
        game.load_game()
    elif option == "0":
        sys.exit(0)
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
