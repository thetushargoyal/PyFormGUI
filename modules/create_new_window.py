import tkinter as tk


def createNewWindow(label_val, window_name, photo, font_name = 'Arial', font_size = 11, current_x = 10, current_y = 100):

    def newWindow(window_name = window_name, label_val = label_val): 
        top2 = tk.Toplevel(window_name)
        top2.title(label_val)
        width= top2.winfo_screenwidth()
        height= top2.winfo_screenheight()

        #setting tkinter window size
        top2.geometry("%dx%d" % (width, height))

        mystr = tk.StringVar()
        mystr.set('1')

        tk.Button(top2,text='OK',width=10,command=top2.destroy).pack(pady=8)

        top2.transient(window_name)
        top2.grab_set()
        window_name.wait_window(top2)

    def infoBox():
        tk.messagebox.showinfo("Number of Harts","Description: Total number of harts to be instantiated in the dummy test-soc. Note that these will non-coherent cores simply acting as windows on the fast-bus.")

    font_val = font_name + " " + str(font_size)
    state = 'normal'

    label = tk.Label(window_name, text = label_val, font= font_val)
    label.place(x = current_x, y =current_y)
    window_name.update()
    width = label.winfo_width()
    tk.Button(window_name, image = photo, command = infoBox,  relief = 'flat').place(x=current_x + width, y=current_y+3)

    tk.Button(window_name, text ="Configure", command = newWindow).place(x = current_x + width + 40, y = current_y)