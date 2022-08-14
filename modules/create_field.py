import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import modules.config as config

import os

image_path = str(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'images', 'info_icon.png')))

icon = tk.PhotoImage(file = image_path)

def createFrame(window_frame_name, padx=(0,0), pady=(0,0), side='left', fill = 'none'):
    frame = tk.Frame(window_frame_name)
    frame.pack(padx = padx, pady=pady, side=side, fill=fill)
    return frame

def make_label(label_val, font_val, frame, _infobox):
    label = tk.Label(frame, text = label_val, font= font_val)
    if (_infobox == True):
        label.pack(side = 'left', padx=(10, 0))
    else:
        label.pack(side = 'left', padx=(10, 20))
    return label

def createInfoBox(_infobox, heading, description, frame, photo = icon):
    def infoBox():
        tkinter.messagebox.showinfo(heading, description)

    if (_infobox == True):
        tk.Button(frame, image = photo, command = infoBox,  relief = 'flat').pack(side = 'left', padx=(0, 20))

def createLabel(label_val, font_name = 'Arial', font_size = 11, _infobox = False, heading = '', description = '', window_name = config.window):

    font_val = font_name + " " + str(font_size)

    frame = tk.Frame(window_name)

    frame.pack(pady=(0, 10), side = 'top', fill='x')

    make_label(label_val, font_val, frame, _infobox)
    
    createInfoBox(_infobox, heading, description, frame)   

def createTextEntry(label_val, font_name = 'Arial', font_size = 11, default_fixed = False, fixed_val = '', _infobox = False, heading = '', description = '', numbers_only = False, window_name = config.window):

    font_val = font_name + " " + str(font_size)
    state = 'normal'

    mystr = tk.StringVar()
    if (fixed_val != ''):
        mystr.set(fixed_val)

    if (default_fixed == True):
        mystr.set(fixed_val)
        state='readonly'

    frame = createFrame(window_name, side='top', fill='x', pady=(0, 10))

    make_label(label_val, font_val, frame, _infobox)
    
    createInfoBox(_infobox, heading, description, frame) 

    if (numbers_only == True):
        def validate(u_input): # callback function
            return u_input.isdigit()
        my_valid = window_name.register(validate)
        tk.Entry(frame,textvariable=mystr, state=state, font=(font_name, font_size,'normal'), justify='center', width= 10, validate='key',validatecommand=(my_valid,'%S')).pack(side = 'left')
    else:
        tk.Entry(frame,textvariable=mystr, state=state, font=(font_name, font_size,'normal'), justify='center', width = 10).pack(side = 'left')

    return mystr

def createTrueFalse(label_val, 
                    window_name,
                    font_name = 'Arial', 
                    font_size = 11, 
                    default_fixed = False, 
                    fixed_val = False,
                    _infobox = False, 
                    heading = '', 
                    description = '',):

    font_val = font_name + " " + str(font_size)
    state = 'normal'

    mystr = tk.BooleanVar(window_name)
    if (default_fixed == True):
        mystr.set(fixed_val)
        state='disabled'

    style = ttk.Style()
 
    style.configure('TRadiobutton', font = (font_name, font_size))

    frame = createFrame(window_name, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')

    make_label(label_val, font_val, frame_1, _infobox)
    
    createInfoBox(_infobox, heading, description, frame_1)

    ttk.Radiobutton(frame,  text = "True", state=state, variable = mystr, value = True).pack(side = 'left', padx=(0, 10))
    ttk.Radiobutton(frame,  text = "False", state=state, variable = mystr, value = False).pack(side = 'left')

    return mystr

def createDropDown(option_list, label_val, font_val, _infobox = False, heading = '', description = '', window_name = config.window):

    mystr = tk.StringVar()

    frame = createFrame(window_name, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')

    make_label(label_val, font_val, frame_1, _infobox)
    
    createInfoBox(_infobox, heading, description, frame_1)

    dropDown = ttk.Combobox(frame, width = 15, textvariable = mystr, justify='center', state='readonly')
    dropDown.bind("<<ComboboxSelected>>",lambda e: window_name.focus())

    dropDown['values'] = option_list
    
    dropDown.pack(side = 'left')

    return mystr

def createCounterField(label_val, font_val, window_name, _infobox = False, heading = '', description = ''):

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

    frame = createFrame(window_name, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')

    make_label(label_val, font_val, frame_1, _infobox)
    
    createInfoBox(_infobox, heading, description, frame_1)

    frame_2 = createFrame(frame, side='left')

    def validate(u_input): # callback function
        return u_input.isdigit()
    my_valid = window_name.register(validate)

    counter_entry = tk.Entry(frame_2, font=('Arial',11),justify='center', width= 6, validate='key',validatecommand=(my_valid,'%S'))
    counter_entry.insert(0, 0)
    increment_counter = tk.Button(frame_2, command = increment, text='+', width= 2)
    decrement_counter = tk.Button(frame_2, command = decrement, text='-', width=2)

    decrement_counter.pack(side = 'left')
    counter_entry.pack(side = 'left', padx=7)
    increment_counter.pack(side = 'left')

    return int(counter_entry.get())

def createWindow(frame, window_name = config.window):
    top2 = tk.Toplevel(window_name,  background='red')
    top2.title("TopLevel Window")
    window_frame = createFrame(top2, side = 'top', fill = 'both')

    def hide():
        top2.grab_release()
        top2.withdraw()

    top2.protocol('WM_DELETE_WINDOW', hide)  
    top2.withdraw()

    def show():
        top2.grab_set()
        top2.deiconify()
        
    tk.Button(frame, command = show, text='+', width=2).pack()

    return window_frame