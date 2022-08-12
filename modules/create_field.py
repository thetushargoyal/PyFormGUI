import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import modules.config as config

icon = tk.PhotoImage(file = r"C:\Users\Tushar\Desktop\Work\PyFormGUI\images\info_icon.png")

def make_label(label_val, font_val, setoff, window_name = config.window):
    
    label = tk.Label(window_name, text = label_val, font= font_val)
    label.place(x = config.current_x + setoff, y = config.current_y)
    window_name.update()
    return label

def createInfoBox(_infobox, heading, description, width, photo = icon, window_name = config.window):

    def infoBox():
        tkinter.messagebox.showinfo(heading, description)

    if (_infobox == True):
        tk.Button(window_name, image = photo, command = infoBox,  relief = 'flat').place(x=config.current_x + width, y=config.current_y+3)

def createLabel(label_val, font_name = 'Arial', font_size = 11, _infobox = False, heading = '', description = '', setoff = 0, window_name = config.window):

    font_val = font_name + " " + str(font_size)

    label = make_label(window_name, label_val, font_val, setoff)
    width = label.winfo_width()
    
    createInfoBox(_infobox, heading, description, width)   
    window_name.update()

    config.update_config()

def createTextEntry(label_val, font_name = 'Arial', font_size = 11, default_fixed = False, fixed_val = '', _infobox = False, heading = '', description = '', setoff = 0, numbers_only = False, window_name = config.window):

    font_val = font_name + " " + str(font_size)
    state = 'normal'

    mystr = tk.StringVar()
    if (fixed_val != ''):
        mystr.set(fixed_val)

    if (default_fixed == True):
        mystr.set(fixed_val)
        state='readonly'

    label = make_label(label_val, font_val, setoff)
    width = label.winfo_width()

    createInfoBox(_infobox, heading, description, width)

    if (numbers_only == True):
        def validate(u_input): # callback function
            return u_input.isdigit()
        my_valid = window_name.register(validate)
        tk.Entry(window_name,textvariable=mystr, state=state, font=(font_name, font_size,'normal'), justify='center', validate='key',validatecommand=(my_valid,'%S')).place(x = config.current_x + width + 40, y = config.current_y, width= 100, height = 20)
    else:
        tk.Entry(window_name,textvariable=mystr, state=state, font=(font_name, font_size,'normal'), justify='center').place(x = config.current_x + width + 40, y = config.current_y, width= 100, height = 20)

    window_name.update()

    config.update_config()

    return mystr

def createTrueFalse(label_val, 
                    font_name = 'Arial', 
                    font_size = 11, 
                    default_fixed = False, 
                    fixed_val = 0,
                    _infobox = False, 
                    heading = '', 
                    description = '',
                    setoff = 0, 
                    window_name = config.window):

    font_val = font_name + " " + str(font_size)
    state = 'normal'

    mystr = tk.IntVar(window_name, 0)
    if (default_fixed == True):
        mystr.set(fixed_val)
        state='disabled'

    style = ttk.Style()
 
    style.configure('TRadiobutton', font = (font_name, font_size))

    label = make_label(label_val, font_val, setoff)
    width = label.winfo_width()

    createInfoBox(_infobox, heading, description, width + setoff)

    ttk.Radiobutton(window_name,  text = "True", state=state, variable = mystr, value = 1).place(x = config.current_x + width + 40 + setoff, y =config.current_y)
    ttk.Radiobutton(window_name,  text = "False", state=state, variable = mystr, value = 0).place(x = config.current_x + width + 100 + setoff, y =config.current_y)

    config.update_config()

def createDropDown(option_list, label_val, font_val, _infobox = False, heading = '', description = '', setoff = 0, window_name = config.window):

    mystr = tk.StringVar()
    dropDown = ttk.Combobox(window_name, width = 15, textvariable = mystr, justify='center', state='readonly')
    dropDown.bind("<<ComboboxSelected>>",lambda e: window_name.focus())

    dropDown['values'] = option_list
    
    label = make_label(label_val, font_val, setoff)
    width = label.winfo_width()
    
    createInfoBox(_infobox, heading, description, width)

    dropDown.place(x = config.current_x + width + 40, y = config.current_y + 3)

    config.update_config()

    return mystr

def createCounterField(label_val, font_val, _infobox = False, heading = '', description = '', setoff = 0, window_name = config.window):

    def increment():
        counter = int(counter_entry.get())
        counter += 1
        counter_entry.delete(0, tk.END)
        counter_entry.insert(0, counter)

    def decrement():
        counter = int(counter_entry.get())
        if (counter > 0):
            counter -= 1
            counter_entry.delete(0, tk.END)
            counter_entry.insert(0, counter)

    def validate(u_input): # callback function
        return u_input.isdigit()
    my_valid = window_name.register(validate)

    counter_entry = tk.Entry(window_name, font=('Arial',11),justify='center', width= 5, validate='key',validatecommand=(my_valid,'%S'))
    counter_entry.insert(0, 0)
    increment_counter = tk.Button(window_name, command = increment, text='+', width= 2)
    decrement_counter = tk.Button(window_name, command = decrement, text='-', width=2)

    label = make_label(label_val, font_val, setoff)
    width = label.winfo_width()

    createInfoBox(_infobox, heading, description, width)

    decrement_counter.place(x = width + 40 + config.current_x, y = config.current_y)
    counter_entry.place(x = width + 40 + config.current_x + 40, y = config.current_y + 3)
    increment_counter.place(x = width + 40 + config.current_x + 100, y = config.current_y)
    
    config.update_config()

    return int(counter_entry.get())