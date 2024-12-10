from tkinter import *
from tkinter import ttk
from colours import ProjectColours
import re


class Calculator:

    def __init__(self, root, display_frame, historic_frame):

        self.root = root
        self.fr_display = display_frame
        self.fr_historic = historic_frame

        self.equation = StringVar()
        self.label_value = ''

        self.root.bind('<Key>', self.key_press)

        self.display_number()

        self.historic()

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

    def clean_historic(self):
        self.historic_listbox.delete(0, END)

    def clean_equation(self, expression):
        self.cleaned_expression = re.sub(r'\b0+(?=\d)', '', expression)
        return self.cleaned_expression

    def results(self):
        try:

            self.cleaned_equation = self.clean_equation(self.equation.get())

            self.result = eval(self.cleaned_equation)

            if isinstance(self.result, float) and self.result.is_integer():
                self.equation.set(int(self.result))
                self.result = int(self.result)

            elif isinstance(self.result, float):
                self.equation.set(round(self.result, 1))
                self.result = round(self.result, 1)

            else:
                self.equation.set(self.result)

            self.historic_listbox.insert(
                END, f'{self.label_value} = {str(self.result)}')
            self.label_value = str(self.result)

        except ZeroDivisionError:
            self.equation.set('Divisão por 0 inválida')
            self.label_value = ''

        except Exception as e:
            self.equation.set('Error')
            print(f'Erro: {e}')
            self.label_value = ''

    def historic(self):

        self.historic_listbox = Listbox(
            self.fr_historic, width=25, height=20, bg=ProjectColours.colours['blue_light'], fg=ProjectColours.colours['white'], font=('Ivy', 13), selectbackground=ProjectColours.colours['blue_light'])
        self.historic_listbox.pack(
            side=LEFT, fill=BOTH, expand=True)
        self.historic_listbox.focus_set()
        self.historic_listbox.bind(
            '<<ListboxSelect>>', self.get_value_historic)

    def get_value_historic(self, event):
        self.value = self.historic_listbox.get(
            self.historic_listbox.curselection())
        self.formatted_value = self.value.split('=')[1].strip()
        self.equation.set(self.formatted_value)
        self.label_value = self.formatted_value
