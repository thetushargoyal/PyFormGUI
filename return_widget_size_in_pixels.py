

#Import the required libraries
import tkinter as tk

def returnPixels(label_val, font_val):

    #Create an instance of Tkinter Frame
    win = tk.Tk() 
    #Set the geometry
    win.geometry("700x350")
    
    #Set the default color of the window
    win.config(bg='#aad5df')
    
    #Create a Label to display the text
    label=tk.Label(win, text= label_val,font= (font_val))
    label.pack(pady = 50)
    
    win.update()
    
    #Return and print the width of label widget
    width = label.winfo_width()

    return width

x = returnPixels('sexy', 'Arial 12')
print(x)
 
