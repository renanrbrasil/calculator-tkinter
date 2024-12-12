from tkinter import *
import re
from calculator_colours import ProjectColours


class Calculator:

    """
    A calculator application that handles equation input, evaluation, and history.

    Attributes:
        root (Tk): Main Tkinter window.
        fr_display (Frame): Frame for displaying the current equation.
        fr_historic (Frame): Frame for displaying the calculation history.
        equation (StringVar): Stores the current equation.
        label_value (str): Current equation string being typed.
    """

    def __init__(self, root, display_frame, historic_frame):

        self.root = root
        self.fr_display = display_frame
        self.fr_historic = historic_frame

        # StringVar to hold the current equation, displayed in the UI.
        self.equation = StringVar()

        # Variable to store the equation being typed (as a string).
        self.label_value = ''

        # Bind the key press event to the key_press method for keyboard input.
        self.root.bind('<Key>', self.key_press)

        # Initialize the number display area.
        self.display_number()

        # Initialize the history display area.
        self.historic()

    def display_number(self):
        """
         Creates and places a label in the display frame that shows the current equation.
        """
        self.lb_numbers = Label(self.fr_display, textvariable=self.equation, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=(
            'Ivy', 18), bg=ProjectColours.colours['midnight_blue'], fg=ProjectColours.colours['white'])
        self.lb_numbers.place(x=0, y=0)

    def value_setter(self, value=None):
        """
        Appends the given value to the equation string and updates the displayed equation.

        Parameters:
            value (str): The value to be added to the equation.
        """

        # Append the value to the current equation.
        self.label_value += str(value)

        # Update the equation displayed in the UI.
        self.equation.set(self.label_value)

    def key_press(self, event):
        """
        The method checks the key pressed and calls the appropriate function to update the equation or handle backspace/enter functionality.

        Parameters:
            event (Event): The event object containing the key pressed.
        """

        key = event.char
        # Check if the key pressed is a number or an operator, and append it to the equation.
        if key in '0123456789' or key in '*/+-.':
            self.value_setter(key)

        # Handle backspace key: remove the last character from the equation.
        elif event.keysym == 'BackSpace':
            if len(self.label_value) > 0:
                self.label_value = self.label_value[:-1]
                self.equation.set(self.label_value)

        # Handle Enter key: calculate the result of the equation if the equation is not empty.
        elif event.keysym == 'Return':
            if len(self.label_value.strip()) > 0:
                self.results()

    def clean_screen(self):
        """
        This method resets the equation string to an empty state.
        """

        # Clear the current equation string and update the UI.
        self.label_value = ''
        self.equation.set(self.label_value)

    def clean_historic(self):
        """
        This method removes all entries from the historic list box, clearing the history.
        """

        # Clear all items in the history listbox.
        self.historic_listbox.delete(0, END)

    def clean_equation(self, expression):
        """
        This method uses a regular expression to remove any leading zeros in numbers within the equation and validates an input expression.

        Parameters:
            expression (str): The equation string to be cleaned.

        Returns:
            str: The cleaned equation without leading zeros.
        """

        # Input validation: Only numbers, signals, and parentheses are allowed.
        if not re.match(r'^[0-9+\-*/().]*$', expression):
            raise ValueError("Expressão inválida")

        # Use regex to remove leading zeros in the equation.
        self.cleaned_expression = re.sub(r'\b0+(?=\d)', '', expression)
        return self.cleaned_expression

    def results(self):
        """
        This method attempts to calculate the result of the current equation. If successful, it updates 
        the display with the result and adds the equation to the history. If there is an error, an error message is shown.

        Handles:
            - ZeroDivisionError: Displays 'Divisão por 0 inválida'.
            - Any other exception: Displays 'Error'.
        """

        try:

            # A dict with restrictions for eval, allowing only specific math functions and operators.
            # Disables built-ins and includes handling for division by zero.
            safe_dict = {
                '__builtins__': None,
                'abs': abs,
                'round': round,
                'max': max,
                'min': min,
                'pow': pow,
                'int': int,
                'float': float,
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y if y != 0 else 'Divisão por 0 inválida',
                '**': lambda x, y: x ** y,
                '%': lambda x, y: x % y
            }

            # Clean the equation from leading zeros.
            self.cleaned_equation = self.clean_equation(self.equation.get())

            # Evaluate the equation using the eval function.
            self.result = eval(self.cleaned_equation, safe_dict)

            # If the result is a float, round it or convert it to an integer if it's a whole number.
            if isinstance(self.result, float) and self.result.is_integer():
                self.equation.set(int(self.result))
                self.result = int(self.result)

            elif isinstance(self.result, float):
                self.equation.set(round(self.result, 1))
                self.result = round(self.result, 1)

            else:
                self.equation.set(self.result)

            # Add the equation and result to the history listbox.
            self.historic_listbox.insert(
                END, f'{self.label_value} = {str(self.result)}')

            # Update the label value with the result.
            self.label_value = str(self.result)

            if self.result == '':
                self.equation.set('0')

        except ZeroDivisionError:
            # Handle division by zero error.
            self.equation.set('Divisão por 0 inválida')
            self.label_value = ''

        except Exception:
            # Handle any other errors and display an error message.
            self.equation.set('Error')
            self.label_value = ''

    def historic(self):
        """
        Displays the history of previous calculations and is linked to an event handler for selecting an entry from history.
        """

        # Create and configure the history listbox.
        self.historic_listbox = Listbox(
            self.fr_historic, width=25, height=20, bg=ProjectColours.colours['deep_blue'], fg=ProjectColours.colours['white'], font=('Ivy', 13), selectbackground=ProjectColours.colours['deep_blue'])
        self.historic_listbox.pack(
            side=LEFT, fill=BOTH, expand=True)
        self.historic_listbox.focus_set()

        # Bind the history item selection to the event handler.
        self.historic_listbox.bind(
            '<<ListboxSelect>>', self.get_value_historic)

    def get_value_historic(self, event):
        """
        When an item from the history is selected, this method updates the current equation display with the selected result.

        Parameters:
            event (Event): The event triggered when an item is selected from the history list box.
        """

        # Retrieve the selected item from the history listbox.
        self.value = self.historic_listbox.get(
            self.historic_listbox.curselection())

        # Extract the result part from the history item.
        self.formatted_value = self.value.split('=')[1].strip()

        # Set the equation to the selected result.
        self.equation.set(self.formatted_value)
        self.label_value = self.formatted_value
