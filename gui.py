# gui.py
from tkinter import Tk, Label, Button, Entry, Checkbutton, IntVar, StringVar, Scale
from password_generator import PasswordGenerator  # Import the PasswordGenerator class

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.generator = PasswordGenerator()
        self.build_ui()

    def build_ui(self):
        # Create the UI components (labels, sliders, checkboxes, etc.)
        self.length_label = Label(self.master, text="Password Length:")
        self.length_label.grid(row=0, column=0)
        
        self.length_slider = Scale(self.master, from_=12, to=20, orient="horizontal")
        self.length_slider.grid(row=0, column=1)

        # Checkboxes for character options
        self.uppercase_var = IntVar()
        self.uppercase_check = Checkbutton(self.master, text="Include Uppercase", variable=self.uppercase_var)
        self.uppercase_check.grid(row=1, column=0)
        
        self.lowercase_var = IntVar()
        self.lowercase_check = Checkbutton(self.master, text="Include Lowercase", variable=self.lowercase_var)
        self.lowercase_check.grid(row=2, column=0)

        self.numbers_var = IntVar()
        self.numbers_check = Checkbutton(self.master, text="Include Numbers", variable=self.numbers_var)
        self.numbers_check.grid(row=3, column=0)

        self.symbols_var = IntVar()
        self.symbols_check = Checkbutton(self.master, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.grid(row=4, column=0)

        # Generate Button
        self.generate_button = Button(self.master, text="Generate Password", command=self.on_generate_click)
        self.generate_button.grid(row=5, column=0, columnspan=2)

        # Textbox to display generated password
        self.password_display = Entry(self.master, state="readonly")
        self.password_display.grid(row=6, column=0, columnspan=2)

    def on_generate_click(self):
        # Collect user inputs and generate the password
        length = self.length_slider.get()
        self.generator.add_character_pool(
            self.uppercase_var.get(), 
            self.lowercase_var.get(), 
            self.numbers_var.get(), 
            self.symbols_var.get()
        )
        try:
            password = self.generator.generate(length)
            self.password_display.config(state="normal")
            self.password_display.delete(0, "end")
            self.password_display.insert(0, password)
            self.password_display.config(state="readonly")
        except ValueError as e:
            self.password_display.config(state="normal")
            self.password_display.delete(0, "end")
            self.password_display.insert(0, str(e))
            self.password_display.config(state="readonly")
