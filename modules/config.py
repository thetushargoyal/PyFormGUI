import tkinter as tk
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

current_x = 15
current_y = 70

def update_config():
    global current_x, current_y
    if (current_y < height - 100):
        current_y = current_y + 30
    else: 
        current_y = 50
        current_x = 500

def run_window(window = window):
    window.mainloop()
