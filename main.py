# main.py
from tkinter import Tk
from gui import MainApp  # Import MainApp class from gui.py
# import pyperclip  # Uncomment if clipboard functionality is needed

if __name__ == "__main__":
    root = Tk()  # Create the main window
    app = MainApp(root)  # Initialize the GUI application
    root.mainloop()  # Start the Tkinter event loop
