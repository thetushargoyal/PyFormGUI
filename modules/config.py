import tkinter as tk

#creating window
window = tk.Tk() 

#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()

#setting tkinter window size
window.geometry("%dx%d" % (width, height))

# setting attribute
window.state('zoomed')
window.title("Configure Chromite Core")

current_x = 20
current_y = 50

def update_config():
    global current_x, current_y
    if (current_y < height - 100):
        current_y = current_y + 30
    else: 
        current_y = 50
        current_x = 500