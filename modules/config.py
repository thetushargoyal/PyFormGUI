import tkinter as tk
from tkinter import ttk
import platform

#creating window
window = tk.Tk() 

#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

#setting tkinter window size
window.geometry("%dx%d" % (width, height))

# setting attribute

if (platform.system() == 'Windows' or platform.system() == "Darwin"):
    window.state('zoomed')
elif (platform.system() == 'Linux'):
    window.attributes('-zoomed', True)
else:
    window.state('normal')

window.title("Configure Chromite Core")

def run_window(window = window):
    window.mainloop()

font_val = 'Arial 11'