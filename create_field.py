import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import config

icon = tk.PhotoImage(file = r"C:\Users\Tushar\Desktop\Work\InCore Semiconductors\images\info_icon.png")

def make_label(window_name, label_val, font_val, setoff):
    
    label = tk.Label(window_name, text = label_val, font= font_val)
    label.place(x = config.current_x + setoff, y = config.current_y)
    window_name.update()
    return label

def createLabel(label_val, window_name, photo = icon, font_name = 'Arial', font_size = 11, _infobox = False, heading = '', description = '', setoff = 0):


    font_val = font_name + " " + str(font_size)
    state = 'normal'


    label = make_label(window_name, label_val, font_val, setoff)
    width = label.winfo_width()
    createInfoBox(_infobox, heading, description, window_name, photo, width)   
    window_name.update()

    config.update_config()

def createInfoBox(_infobox, heading, description, window_name, photo, width):


    def infoBox():
        tkinter.messagebox.showinfo(heading, description)

    if (_infobox == True):
        tk.Button(window_name, image = photo, command = infoBox,  relief = 'flat').place(x=config.current_x + width, y=config.current_y+3)

def createTextEntry(label_val, window_name, photo = icon, font_name = 'Arial', font_size = 11, default_fixed = False, fixed_val = '', _infobox = False, heading = '', description = '', setoff = 0, numbers_only = False):


    font_val = font_name + " " + str(font_size)
    state = 'normal'

    mystr = tk.StringVar()
    if (fixed_val != ''):
        mystr.set(fixed_val)

    if (default_fixed == True):
        mystr.set(fixed_val)
        state='readonly'

 # register 

    total_width = 0

    label = make_label(window_name, label_val, font_val, setoff)
    width = label.winfo_width()
    height = label.winfo_height()
    createInfoBox(_infobox, heading, description, window_name, photo, width)

    if (numbers_only == True):
        def validate(u_input): # callback function
            return u_input.isdigit()
        my_valid = window_name.register(validate)
        tk.Entry(window_name,textvariable=mystr, state=state, font=(font_name, font_size,'normal'), justify='center', validate='key',validatecommand=(my_valid,'%S')).place(x = config.current_x + width + 40, y = config.current_y, width= 100, height = 20)
    else:
        tk.Entry(window_name,textvariable=mystr, state=state, font=(font_name, font_size,'normal'), justify='center').place(x = config.current_x + width + 40, y = config.current_y, width= 100, height = 20)


    
    
    window_name.update()


    total_width = 0

    config.update_config()


    return mystr

def createTrueFalse(label_val, 
                    window_name, 
                    photo = icon,
                    font_name = 'Arial', 
                    font_size = 11, 
                    default_fixed = False, 
                    fixed_val = 0,
                    _infobox = False, 
                    heading = '', 
                    description = '',
                    setoff = 0):

    font_val = font_name + " " + str(font_size)
    state = 'normal'

    mystr = tk.IntVar(window_name, 0)
    if (default_fixed == True):
        mystr.set(fixed_val)
        state='disabled'

    style = ttk.Style()
 
    style.configure('TRadiobutton', font = (font_name, font_size))


    label = make_label(window_name, label_val, font_val, setoff)
    width = label.winfo_width()
    createInfoBox(_infobox, heading, description, window_name, photo, width + setoff)
    ttk.Radiobutton(window_name,  text = "True", state=state, variable = mystr, value = 1).place(x = config.current_x + width + 40 + setoff, y =config.current_y)
    ttk.Radiobutton(window_name,  text = "False", state=state, variable = mystr, value = 0).place(x = config.current_x + width + 100 + setoff, y =config.current_y)

    config.current_y = config.current_y + 30

def createDropDown(window_name, option_list, label_val, font_val, photo = icon, _infobox = False, heading = '', description = '', setoff = 0):

    mystr = tk.StringVar()
    dropDown = ttk.Combobox(window_name, width = 15, textvariable = mystr, justify='center', state='readonly')
    dropDown.bind("<<ComboboxSelected>>",lambda e: window_name.focus())
    # Adding combobox drop down list
    dropDown['values'] = option_list
    
    label = make_label(window_name, label_val, font_val, setoff)
    width = label.winfo_width()
    createInfoBox(_infobox, heading, description, window_name, photo, width)
    dropDown.place(x = config.current_x + width + 40, y = config.current_y + 3)
    config.current_y = config.current_y + 30

    return mystr

def createCounterField(window_name, label_val, font_val, photo = icon, _infobox = False, heading = '', description = '', setoff = 0):

    counter_var=tk.IntVar(value=0)

    def increment():
    
        counter = counter_var.get()
        counter += 1
        counter_var.set(counter)

    def decrement():
    
        counter = counter_var.get()
        if (counter > 0):
            counter -= 1
            counter_var.set(counter)

    counter_entry = tk.Entry(window_name,textvariable = counter_var, font=('calibre',10,'normal'),justify='center', width= 5)
    increment_counter = tk.Button(window_name, command = increment, text='+', width= 2)
    decrement_counter = tk.Button(window_name, command = decrement, text='-', width=2)

    label = make_label(window_name, label_val, font_val, setoff)
    width = label.winfo_width()
    createInfoBox(_infobox, heading, description, window_name, photo, width)

    increment_counter.place(x = width + 40 + config.current_x + 90, y = config.current_y)

    counter_entry.place(x = width + 40 + config.current_x + 40, y = config.current_y + 3)
    
    decrement_counter.place(x = width + 40 + config.current_x, y = config.current_y)

    config.current_y = config.current_y + 30

    return counter_var