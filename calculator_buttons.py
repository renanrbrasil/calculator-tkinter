from tkinter import Button, RIDGE, RAISED
from calculator_colours import ProjectColours
from calculator_logic import Calculator


class TkinterButtons:

    """
    This class is responsible for creating and managing the buttons in the calculator application.

    Attributes:
        root (Tk): The main Tkinter window instance.
        fr_display (Frame): Frame where numbers and equations are displayed.
        fr_body (Frame): Frame containing the numeric and operator buttons.
        fr_historic (Frame): Frame showing the history of calculations.
        button_command (Calculator): Object responsible for handling button commands and calculator logic.
        button_params (list): List of dictionaries, each containing configuration details for a button.
    """

    def __init__(self, root, display_frame, body_frame, historic_frame):
        """
        Initializes the TkinterButtons class and sets up the button configuration.

        Parameters:
            root (Tk): The main Tkinter window instance.
            display_frame (Frame): The frame where numbers and equations are displayed.
            body_frame (Frame): The frame where numeric buttons and mathematical operators are placed.
            historic_frame (Frame): The frame where the calculation history is shown.

        This constructor also initializes the Calculator logic object to handle button operations.
        """

        self.root = root
        self.fr_display = display_frame
        self.fr_body = body_frame
        self.fr_historic = historic_frame

        # Initialize the button command logic for handling button operations
        self.button_command = Calculator(
            self.root, self.fr_display, self.fr_historic)

        self.create_button()

    def create_numbers_buttons(self):
        """
        Generates a list of dictionaries containing configurations for numeric buttons (1-9), each button is positioned in a 3x3 grid layout, and each configuration contains properties such as size, color, and command action.

        Returns:
            list: A list of dictionaries, each representing a button's configuration.
        """

        # List where the button settings will be stored.
        number_buttons = []

        # Defines the 'y' positions of the rows
        y_positions = [156, 104, 52]

        # Defines the 'x' positions of the rows
        x_positions = [0, 59, 119]

        # List of button numbers (1 to 9)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Loops to iterate over the lines (y_positions) and (x_positions)
        for i, y in enumerate(y_positions):
            for j, x in enumerate(x_positions):

                # Calculates the button number based on the position indices (i, j)
                number = numbers[i * 3 + j]

                # Adds the button settings to the number_buttons list
                number_buttons.append({
                    'frame': self.fr_body,
                    'text': number,
                    'width': 5,
                    'height': 2,
                    'bg': ProjectColours.colours['blue_gray'],
                    'fg': ProjectColours.colours['white'],
                    'x_position': x,
                    'y_position': y,
                    'command': lambda value=number: self.button_command.value_setter(value)
                })

        return number_buttons

    def create_signals_buttons(self):
        """
        Creates a list of dictionaries for signal buttons ('/', '*', '-', '+') 
        with predefined positions and configurations.

        Returns:
            list: A list of dictionaries for signal button configurations.
        """

        # List where the button settings will be stored.
        signal_buttons = []

        # List of buttons position
        positions = [
            ('/', 177, 0),
            ('*', 177, 52),
            ('-', 177, 104),
            ('+', 177, 156)
        ]

        # Loop to create the signal buttons params
        for signal, x, y in positions:
            signal_buttons.append({
                'frame': self.fr_body,
                'text': signal,
                'width': 5,
                'height': 2,
                'bg': ProjectColours.colours['deep_blue'],
                'fg': ProjectColours.colours['white'],
                'x_position': x,
                'y_position': y,
                'command': lambda value=signal: self.button_command.value_setter(value)
            })

        return signal_buttons

    def create_special_buttons(self):
        """
        Creates a list of dictionaries for special buttons ('C', '%', '0', '.', '=', 'CE') with their respective configurations.

        Returns:
        list: A list of dictionaries for special button configurations.
        """

        # List where the button settings will be stored.
        special_buttons = []

        # Define button properties (text, x, y, width, height, command)
        button_data = [
            ('C', 0, 0, 11, 2, self.button_command.clean_screen,
             ProjectColours.colours['blue']),
            ('%', 118, 0, 5, 2, lambda value='%': self.button_command.value_setter(
                value), ProjectColours.colours['blue_gray']),
            ('0', 0, 208, 11, 2, lambda value='0': self.button_command.value_setter(
                value), ProjectColours.colours['blue_gray']),
            ('.', 119, 208, 5, 2, lambda value='.': self.button_command.value_setter(
                value), ProjectColours.colours['blue_gray']),
            ('=', 177, 208, 5, 2, self.button_command.results,
             ProjectColours.colours['orange']),
            ('CE', 0.5, 260.6, 12, 2,
             lambda: (self.button_command.clean_historic(),
                      self.button_command.clean_screen()),
             ProjectColours.colours['blue'])
        ]

        # Loop to create the special buttons params
        for text, x, y, width, height, command, bg in button_data:
            special_buttons.append({
                'frame': self.fr_body if text != 'CE' else self.fr_historic,
                'text': text,
                'width': width,
                'height': height,
                'bg': bg,
                'fg': ProjectColours.colours['white'],
                'x_position': x,
                'y_position': y,
                'command': command
            })

        return special_buttons

    def create_button(self):
        """
        This method merges all button_params into a list that contains the dictionaries for each button, and 
        iterates through this list to create each button by calling the button_settings function.
        """

        self.buttons_config = [
            *self.create_numbers_buttons(),

            *self.create_signals_buttons(),

            *self.create_special_buttons()
        ]

        for button_param in self.buttons_config:
            self.button_settings(button_param)

    def button_settings(self, button_params):
        """
        This function uses the attributes in the button_params dictionary to configure and create 
        a Tkinter Button widget. 

        Parameters:
        button_params (dict): A dictionary containing the button's configuration. Expected keys:
            - frame: The parent frame for the button (Tkinter frame).
            - command: The function to be executed when the button is clicked.
            - text: The text to be displayed on the button.
            - width: The width of the button.
            - height: The height of the button.
            - bg: The background color of the button.
            - fg: The foreground (text) color of the button.
            - x_position: The x-coordinate for button placement.
            - y_position: The y-coordinate for button placement.
        """

        # Create the button using the provided parameters
        button = Button(button_params['frame'],
                        command=button_params['command'],
                        text=button_params['text'],
                        width=button_params['width'],
                        height=button_params['height'],
                        bg=button_params['bg'],
                        fg=button_params['fg'],
                        font=('Ivy', 13, 'bold'),
                        activebackground=button_params['bg'],
                        activeforeground=button_params['fg'],
                        relief=RAISED, overrelief=RIDGE,
                        highlightthickness=1)

        # Position the button in the frame
        button.place(x=button_params['x_position'],
                     y=button_params['y_position'])
