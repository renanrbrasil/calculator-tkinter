from tkinter import Tk, Frame
from calculator_colours import ProjectColours


class TkinterWindow:
    """
    This class is responsible for creating and managing the main Tkinter window for the calculator application.

    Attributes:
        root (Tk): The main Tkinter window instance.
        width (int): The width of the window in pixels.
        height (int): The height of the window in pixels.
        fr_display (Frame): The frame for displaying numbers and equations.
        fr_body (Frame): The frame for numeric keys and math signals.
        fr_historic (Frame): The frame for the equations history.
        fr_line (Frame): A thin frame acting as a vertical line separator.
    """

    def __init__(self):

        # Creates the main Tkinter window instance.
        self.root = Tk()

        # Running tkinter window configuration and saving the width and height variables.
        self.width, self.height = self.window_settings()

        # Apply window styling (title, colors, and icon)
        self.window_style()

        # Create and configure the window frames
        self.window_frames()

    def window_settings(self):
        """
        Configures the geometry and size of the main Tkinter window.
        - It Centers the window on the screen.
        - Sets the fixed size for the calculator window.

        Attributes Set:
        self.width (int): The width of the calculator window.
        self.height (int): The height of the calculator window.
        """

        # Set dimensions for the window
        widget_width = 365
        widget_height = 310

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - widget_width) // 2
        y_position = (screen_height - widget_height) // 2

        # Apply geometry and restrict resizing
        self.root.geometry(
            f'{widget_width}x{widget_height}+{x_position}+{y_position}')
        self.root.resizable(False, False)

        return widget_width, widget_height

    def window_style(self):
        """
        Configures the visual style of the calculator's main window.
        - Sets the window title to 'Calculadora'.
        - Applies a background color using the ProjectColours configuration.
        - Adds a custom icon for the application.
        """

        self.root.title('Calculadora')
        self.root.config(bg='black')

        try:
            self.root.iconbitmap('ico/calculator.ico')
        except Exception as e:
            print(f'Icon file not found. Using default application icon.\n{e}')
        

    def window_frames(self):
        """
         Creation and positioning of frames.

        - self.fr_display: Frame at the top for displaying numbers and equations.
        - self.fr_body: Frame in the center for numeric keys and math operators.
        - self.fr_historic: Frame on the right for showing the history of equations.
        - self.fr_line: Thin vertical line separating the main calculator area from the history frame.
        """

        # Frame at the top to display numbers and equations
        self.fr_display = Frame(
            self.root, width=self.width, height=self.height)
        self.fr_display.place(relx=0, rely=0, relwidth=1, relheight=0.17)

        # Frame in the center for numeric keys and math operators
        self.fr_body = Frame(
            self.root, width=self.width, height=self.height, bg='white')
        self.fr_body.place(relx=0, rely=0.172)

        # Frame on the right side to show the history of equations
        self.fr_historic = Frame(
            self.root, width=128, height=310, bg=ProjectColours.colours['midnight_blue'])
        self.fr_historic.place(relx=0.65, rely=0)

        # Thin vertical line separating the main area from the history frame
        self.fr_line = Frame(
            self.root, width=1, height=54, bg='black')
        self.fr_line.place(relx=0.647, rely=0)

    def start_tkinter(self):
        """
        Starts the Tkinter main loop. This method keeps the application running, waiting for user interactions such as button clicks or inputs.
        """
        self.root.mainloop()
