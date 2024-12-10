from tkinter import *
from tkinter import ttk
from tkinter_window import TkinterWindow
from colours import ProjectColours
from calculator_logic import Calculator


class TkinterButtons:

    def __init__(self, root, display_frame, body_frame, historic_frame):

        self.root = root
        self.fr_display = display_frame
        self.fr_body = body_frame
        self.fr_historic = historic_frame

        self.button_command = Calculator(
            self.root, self.fr_display, self.fr_historic)

        self.button_params()

        self.create_button()

    def button_params(self):

        self.button_params = [
            {'frame': self.fr_body, 'text': 'C', 'width': 11, 'height': 2,
             'bg': ProjectColours.colours['light'], 'fg': ProjectColours.colours['white'], 'x_position': 0, 'y_position': 0, 'command': self.button_command.clean_screen},

            {'frame': self.fr_body, 'text': '%', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 119, 'y_position': 0, 'command': lambda value='%': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '/', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_light'], 'fg': ProjectColours.colours['white'], 'x_position': 177, 'y_position': 0, 'command': lambda value='/': self.button_command.value_setter(value)},

            # Botões numéricos com a lógica de lambda
            {'frame': self.fr_body, 'text': '7', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 0, 'y_position': 52, 'command': lambda value='7': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '8', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 59, 'y_position': 52, 'command': lambda value='8': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '9', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 119, 'y_position': 52, 'command': lambda value='9': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '*', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_light'], 'fg': ProjectColours.colours['white'], 'x_position': 177, 'y_position': 52, 'command': lambda value='*': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '4', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 0, 'y_position': 104, 'command': lambda value='4': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '5', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 59, 'y_position': 104, 'command': lambda value='5': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '6', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 119, 'y_position': 104, 'command': lambda value='6': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '-', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_light'], 'fg': ProjectColours.colours['white'], 'x_position': 177, 'y_position': 104, 'command': lambda value='-': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '1', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 0, 'y_position': 156, 'command': lambda value='1': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '2', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 59, 'y_position': 156, 'command': lambda value='2': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '3', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 119, 'y_position': 156, 'command': lambda value='3': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '+', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_light'], 'fg': ProjectColours.colours['white'], 'x_position': 177, 'y_position': 156, 'command': lambda value='+': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '0', 'width': 11, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 0, 'y_position': 208, 'command': lambda value='0': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '.', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['blue_gray'], 'fg': ProjectColours.colours['white'], 'x_position': 118, 'y_position': 208, 'command': lambda value='.': self.button_command.value_setter(value)},

            {'frame': self.fr_body, 'text': '=', 'width': 5, 'height': 2,
             'bg': ProjectColours.colours['orange'], 'fg': ProjectColours.colours['white'], 'x_position': 177, 'y_position': 208, 'command': self.button_command.results},

            {'frame': self.fr_historic, 'text': 'CE', 'width': 12, 'height': 2,
             'bg': ProjectColours.colours['light'], 'fg': ProjectColours.colours['white'], 'x_position': 0.5, 'y_position': 260.6, 'command': lambda: (self.button_command.clean_historic(), self.button_command.clean_screen())}
        ]

    def create_button(self):

        for button_param in self.button_params:
            self.button_settings(button_param)

    def button_settings(self, button_params):

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

        button.place(x=button_params['x_position'],
                     y=button_params['y_position'])

        '''self.historic_listbox.focus_set()'''
