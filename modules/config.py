import tkinter as tk
import platform
import os

class Window():
    window = tk.Tk() # Create the window

    def start_window( window = window, title='', windowIcon = '', fullScreen = False, resizable = True):
        
        if (windowIcon != ''):
            image_path = str(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'assests', windowIcon)))
            window.iconphoto(False, tk.PhotoImage(file=image_path))

        window.title(title)
        
        if (resizable == False):
            window.resizable(False, False)

        if (fullScreen == True):
            if (platform.system() == 'Windows' or platform.system() == "Darwin"):
                window.state('zoomed')
            elif (platform.system() == 'Linux'):
                window.attributes('-zoomed', True)
            else:
                window.state('normal')

        return window

    def end_window(window):
        window.mainloop()

font_val = 'Arial 11'