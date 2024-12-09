from tkinter import *
from tkinter import ttk
from colours import ProjectColours
import re


class Calculator:

    def __init__(self, root, display_frame):

        self.root = root
        self.fr_display = display_frame

        self.equation = StringVar()
        self.label_value = ''

        self.root.bind('<Key>', self.key_press)

        self.display_number()

    def display_number(self):

        self.lb_numbers = Label(self.fr_display, textvariable=self.equation, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=(
            'Ivy', 18), bg=ProjectColours.colours['black_light'], fg=ProjectColours.colours['white'])
        self.lb_numbers.place(x=0, y=0)

    def value_setter(self, value=None):
        self.label_value += str(value)
        self.equation.set(self.label_value)

    def key_press(self, event):
        key = event.char
        if key in '0123456789' or key in '*/+-.':
            self.value_setter(key)

        elif event.keysym == 'BackSpace':
            if len(self.label_value) > 0:
                self.label_value = self.label_value[:-1]
                self.equation.set(self.label_value)

        elif event.keysym == 'Return':
            if len(self.label_value) > 0:
                self.results()

    def clean_screen(self):
        self.label_value = ''
        self.equation.set(self.label_value)

    def clean_equation(self, expression):
        self.cleaned_expression = re.sub(r'\b0+(?=\d)', '', expression)
        return self.cleaned_expression

    def results(self):
        try:

            self.cleaned_equation = self.clean_equation(self.equation.get())

            self.result = eval(self.cleaned_equation)

            if isinstance(self.result, float):
                self.equation.set(f'{self.result:.1f}')
            else:
                self.equation.set(self.result)

            self.label_value = str(self.result)

        except ZeroDivisionError:
            self.equation.set('Divisão por 0 inválida')

        except Exception as e:
            self.equation.set('Error')
            print(f'Erro: {e}')
