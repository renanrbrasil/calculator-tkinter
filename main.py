from tkinter_window import TkinterWindow
from tkinter_buttons import TkinterButtons
from calculator_logic import Calculator


def main():
    main_window = TkinterWindow()

    button_manager = TkinterButtons(main_window.root,
        main_window.fr_display, main_window.fr_body)

    main_window.start_tkinter()


if __name__ == '__main__':
    main()
