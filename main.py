from modules.imports import *

top_line_label = tk.Label(window, text="Configure Your Chromite Core", font= "Arial 15 bold").place(relx = 0.5, rely =0.03, anchor = CENTER)

createTextEntry("No. of Harts", window, fixed_val = '', _infobox = True, heading = 'No. of Harts', description = 'No. of Harts No. of Harts No. of Harts', numbers_only=True)
createTrueFalse("Overlap Redirections", window, _infobox = True, heading= 'Overlap Rediretions', description='Overlap Rediretions Overlap Rediretions Overlap Rediretions')
createCounterField(window, 'No. of Times hit', 'Arial 11')
createDropDown(window, [' -O3', ' -O2', '-O1'], 'Optimization Type', 'Arial 11')
createTextEntry("Text also", window, fixed_val = '', _infobox = True, heading = 'Hello', description = 'What\'s is up Overlap Rediretions Overlap Rediretions Overlap Rediretions')

window.mainloop()