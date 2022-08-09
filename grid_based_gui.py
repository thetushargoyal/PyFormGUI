# importing tkinter for gui
from ctypes import alignment
import tkinter as tk
from tkinter import ttk

# creating window
window = tk.Tk()

#getting screen width and height of display
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
#setting tkinter window size
window.geometry("%dx%d" % (width, height))
 
# setting attribute
window.state('normal')
window.title("Configure Chromite Core")
 
# creating text label to display on window screen
label = tk.Label(window, text="Configure Chromite Core")

name_var=tk.StringVar()
passw_var=tk.StringVar()



# defining a function that will
# get the name and password and
# print them on the screen
def submit():

  name=name_var.get()
  password=passw_var.get()
  
  print("The name is : " + name)
  print("The password is : " + password)
  
  name_var.set("")
  passw_var.set("")
  
  
# creating a label for
# name using widget Label
name_label = tk.Label(window, text = 'No. of Harts', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(window,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
overlap_label = tk.Label(window, text = 'Overlap Redirections', font = ('calibre',10,'bold'))

isb_sizes_label = tk.Label(window, text = 'Overlap ISB Sizes', font = ('calibre',10,'bold'))
isb_s0s1_label = tk.Label(window, text = 'ISB S0S1', font = ('calibre',10,'bold'))
isb_s1s2_label = tk.Label(window, text = 'ISB S1S2', font = ('calibre',10,'bold'))
isb_s2s3_label = tk.Label(window, text = 'ISB S2S3', font = ('calibre',10,'bold'))
isb_s3s4_label = tk.Label(window, text = 'ISB S3S4', font = ('calibre',10,'bold'))
isb_s4s5_label = tk.Label(window, text = 'ISB S4S5', font = ('calibre',10,'bold'))
isb_cachebuffer_label = tk.Label(window, text = 'ISB Cachebuffer', font = ('calibre',10,'bold'))




# placing the label and entry in
# the required position using grid
# method

var = 0
R1 = tk.Radiobutton(window, text="True", variable=var, value=1)

R2 = tk.Radiobutton(window, text="False", variable=var, value=2)

# label
ttk.Label(window, text = "Select the Month :",
          font = ('calibre',10,'bold')).grid(column = 0,
          row = 11, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' Sexy',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
  
monthchoosen.grid(column = 1, row = 11)
monthchoosen.current(1)






name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

overlap_label.grid(row=1,column=0)
R1.grid(row=1, column=1)
R2.grid(row=1, column=2)

isb_sizes_label.grid(row=2, column=0)
isb_s0s1_label.grid(row=3, column=1)
isb_s1s2_label.grid(row=4, column=1)
isb_s2s3_label.grid(row=5, column=1)
isb_s3s4_label.grid(row=6, column=1)
isb_s4s5_label.grid(row=7, column=1)
isb_cachebuffer_label.grid(row=8, column=1)



window.mainloop()

