from modules.imports import *

top_line_label = tk.Label(window, text="Configure Your Chromite Core", font= "Arial 15 bold").place(relx = 0.5, rely =0.03, anchor = CENTER)

createTextEntry("No. of Harts", window, fixed_val = '', _infobox = True, heading = 'Hello', description = 'What\'s is up', numbers_only=True)

createTrueFalse("Overlap Redirections", window, _infobox = True, heading= 'Overlap Rediretions', description='Hola gracis')

createCounterField(window, 'No. of Times hit', 'Arial 11')

createDropDown(window, ['-O3', '-O2', '-O1'], 'Optimization Type', 'Arial 11')

createTextEntry("Text also", window, fixed_val = '', _infobox = True, heading = 'Hello', description = 'What\'s is up')

window.mainloop()