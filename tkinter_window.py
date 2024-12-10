from tkinter import *
from tkinter import ttk
from colours import ProjectColours


class TkinterWindow:
    """
    This class will be responsible to generate the calculator tkinter window.
    """

    def __init__(self):

        # Looping the tkinter window.
        self.root = Tk()

        # Running tkinter window configuration and saving the width and height variables.
        self.width, self.height = self.window_settings()

        # Running tkinter window style.
        self.window_style()

        # Running tkinter window frames.
        self.window_frames()

    def window_settings(self):

        # Takes the monitor screen width and height in pixels.
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Setting the width and height of the tkinter widget
        widget_width = 365
        widget_height = 310

        # Calculate the x and y to centre the window.
        x_position = (screen_width - widget_width) // 2
        y_position = (screen_height - widget_height) // 2

        self.root.geometry(
            f'{widget_width}x{widget_height}+{x_position}+{y_position}')

        self.root.resizable(False, False)

        return widget_width, widget_height

    def window_style(self):

        self.root.title('Calculadora')
        self.root.config(bg=ProjectColours.colours['black'])
        self.root.iconbitmap('ico/calculator.ico')

    def window_frames(self):

        # Frame that displays the numbers and equations.
        self.fr_display = Frame(
            self.root, width=self.width, height=self.height)
        self.fr_display.place(relx=0, rely=0, relwidth=1, relheight=0.17)

        # Frame that displays the numeric keys and math signals.
        self.fr_body = Frame(
            self.root, width=self.width, height=self.height, bg='white')
        self.fr_body.place(relx=0, rely=0.172)

        # Frame that displays the equations historic
        self.fr_historic = Frame(
            self.root, width=128, height=310, bg=ProjectColours.colours['black_light'])
        self.fr_historic.place(relx=0.65, rely=0)

        self.fr_line = Frame(
            self.root, width=1, height=54, bg='black')
        self.fr_line.place(relx=0.647, rely=0)

    def start_tkinter(self):
        self.root.mainloop()
