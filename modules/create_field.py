import tkinter as tk
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
import modules.config as config
import os


image_path = str(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'images', 'info_icon.png')))
icon = tk.PhotoImage(file = image_path)

def createFrame(container, 
                padx=(0,0), 
                pady=(0,0), 
                side='top', 
                fill='none'):

    frame = ttk.Frame(container)
    frame.pack(padx = padx, pady = pady, side = side, fill = fill)

    return frame

def makeLabel(container,
            label_text,  
            font_val,
            infoboxBool,):

    label = ttk.Label(container, text = label_text, font = font_val)

    if (infoboxBool == False):
        label.pack(side = 'left', padx=(0,20))
    else:
        label.pack(side = 'left')

def createInfoBox(container, 
                  infoboxBool, 
                  heading, 
                  description, 
                  photo = icon):

    def infoBox():
        tkinter.messagebox.showinfo(heading, description)
    if (infoboxBool == True):
        tk.Button(container, image = photo, command = infoBox, takefocus=0, relief='flat').pack(side = 'left', padx=(0, 20))

def createLabel(container,
                label_text, 
                infoboxBool = False, 
                heading = '', 
                description = '',
                font_val = config.font_val):

    frame = createFrame(container, pady=(0, 10), side = 'top', fill='x')
    makeLabel(frame, label_text, font_val, infoboxBool)
    createInfoBox(frame, infoboxBool, heading, description) 

def createTextEntry(container,
                    label_text,
                    default_fixed = False, 
                    default_val = '', 
                    infoboxBool = False, 
                    heading = '', 
                    description = '', 
                    numbers_only = False, 
                    font_val = config.font_val):

    state = 'normal'

    frame = createFrame(container, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')
    makeLabel(frame_1, label_text, font_val, infoboxBool)
    createInfoBox(frame_1, infoboxBool, heading, description) 

    if (numbers_only == True):
        def validate(u_input):
            return u_input.isdigit()
        my_valid = container.register(validate) #this can give problem

        mystr = ttk.Entry(frame, state=state, font=font_val, justify='center', width= 10, validate='key',validatecommand=(my_valid,'%S'))
        mystr.pack(side = 'left')
    else:
        mystr = ttk.Entry(frame, state=state, font=font_val, justify='center', width = 10)
        mystr.pack(side = 'left')

    if (default_val != ''):
        mystr.insert(0, default_val)

    if (default_fixed == True):
        mystr.insert(0, default_val)
        mystr.state = 'readonly'

    return mystr

def createTrueFalse(container,
                    label_text, 
                    font_val = config.font_val,
                    default_fixed = False, 
                    default_val = False,
                    infoboxBool = False, 
                    heading = '', 
                    description = ''):

    state = 'normal'

    mystr = tk.BooleanVar(container)
    if (default_fixed == True):
        mystr.set(default_val)
        state='disabled'

    style = ttk.Style()
    style.configure('TRadiobutton', font = font_val)

    frame = createFrame(container, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')
    makeLabel(frame_1, label_text, font_val, infoboxBool)
    createInfoBox(frame_1, infoboxBool, heading, description) 

    ttk.Radiobutton(frame,  text = "True", state=state, variable = mystr, value = True, takefocus=0).pack(side = 'left', padx=(0, 10))
    ttk.Radiobutton(frame,  text = "False", state=state, variable = mystr, value = False, takefocus=0).pack(side = 'left')

    return bool(mystr.get())

def createDropDown(container,
                   option_list, 
                   label_text, 
                   font_val = config.font_val, 
                   infoboxBool = False, 
                   heading = '', 
                   description = '', 
                   window_name = config.window):

    mystr = tk.StringVar()

    frame = createFrame(container, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')
    makeLabel(frame_1, label_text, font_val, infoboxBool)
    createInfoBox(frame_1, infoboxBool, heading, description) 

    style = ttk.Style()
    style.configure('A.TCombobox', font = config.font_val)

    dropDown = ttk.Combobox(frame, width = 15, textvariable = mystr, justify='center', state='readonly', style = 'A.TCombobox')
    dropDown.pack(side = 'left')
    dropDown['values'] = option_list

    dropDown.bind("<<ComboboxSelected>>",lambda e: window_name.focus())

    return str(mystr.get())

def createCounterField(container,
                       label_text, 
                       font_val = config.font_val,
                       default_val = 0, 
                       infoboxBool = False, 
                       heading = '', 
                       description = ''):

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

    frame = createFrame(container, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')
    makeLabel(frame_1, label_text, font_val, infoboxBool)
    createInfoBox(frame_1, infoboxBool, heading, description) 

    frame_2 = createFrame(frame, side='left')

    def validate(u_input):
        return u_input.isdigit()
    my_valid = container.register(validate)
    counter_entry = ttk.Entry(frame_2, font=font_val,justify='center', width= 6, validate='key',validatecommand=(my_valid,'%S'))
    counter_entry.insert(0, default_val)

    style = ttk.Style()
    style.configure('A.TButton', font = config.font_val)

    increment_counter = ttk.Button(frame_2, command = increment, text='+', width= 2, takefocus=0, style = 'A.TButton')
    decrement_counter = ttk.Button(frame_2, command = decrement, text='-', width=2, takefocus=0, style = 'A.TButton')

    decrement_counter.pack(side = 'left')
    counter_entry.pack(side = 'left', padx=7)
    increment_counter.pack(side = 'left')

    return counter_entry

def createWindow(container, 
                 title = 'Enter Title', 
                 label_text = 'New Window', 
                 font_val = config.font_val, 
                 infoboxBool = False,
                 heading='',
                 description=''):

    newWindow = tk.Toplevel(container)
    newWindow.title(title)

    
    def hide():
        newWindow.grab_release()
        newWindow.withdraw()

    newWindow.protocol('WM_DELETE_WINDOW', hide)  
    newWindow.withdraw()


    def show():
        newWindow.grab_current()
        newWindow.deiconify()
        
    
    frame = createFrame(container, side='top', fill='x', pady=(0, 10))

    frame_1 = createFrame(frame, side='left')
    
    makeLabel(frame_1, label_text, font_val, infoboxBool)
    createInfoBox(frame_1, infoboxBool, heading, description) 

    style = ttk.Style()
    style.configure('A.TButton', font = config.font_val)

    ttk.Button(frame, command = show, text='Configure', takefocus=0, style = 'A.TButton').pack(side = 'left')

    return newWindow