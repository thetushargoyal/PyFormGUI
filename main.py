from imports import *

top_line_label = tk.Label(window, text="Configure Your Chromite Core", font= "Arial 15 bold").place(relx = 0.5, rely =0.03, anchor = CENTER)

createTextEntry("No. of Harts", window, fixed_val = '', _infobox = True, heading = 'Hello', description = 'What\'s is up', numbers_only=True)

createTrueFalse("Overlap Redirections", window, _infobox = True, heading= 'Overlap Rediretions', description='Hola gracis')

createTrueFalse("Tushar Goyal", window, _infobox = True, heading= 'Overlap Rediretions', description='Hola gracis')

createCounterField(window, 'No. of Times hit', 'Arial 11')

list_option = ['Tushar', 'Goyal', 'is', 'the', 'best']

createDropDown(window, list_option, 'Names bahag', 'Arial 11')

optimization_type = ['-O3', '-O2', '-O1']

createDropDown(window, optimization_type, 'Optimization Type', 'Arial 11')

createTextEntry("Number of Harts", window, fixed_val = '', _infobox = True, heading = 'Hello', description = 'What\'s is up')

window.mainloop()