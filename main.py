from calculator_window import TkinterWindow
from calculator_buttons import TkinterButtons


def main():
    """
    The main function initializes and starts the Calculator application.

    - Creates the main window using the TkinterWindow class.
    - Initializes buttons with the TkinterButtons class, linking them to the main window components.
    - Starts the Tkinter main loop.
    """

    # Initialize the main window
    main_window = TkinterWindow()

    # Add buttons to the window
    TkinterButtons(main_window.root, main_window.fr_display,
                   main_window.fr_body, main_window.fr_historic)

    # Start the Tkinter application
    main_window.start_tkinter()


if __name__ == '__main__':
    """
    If this module is executed as the main program, 
    calls the main function to start the Calculator application.
    """
    main()
