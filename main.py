from modules.imports import *

top_line_label = tk.Label(window, 
                          text="Configure Your Chromite Core", 
                          font= "Arial 15 bold").place(
                          relx = 0.5, 
                          rely =0.03, 
                          anchor = CENTER)

createTextEntry("No. of Harts",
                fixed_val = '545', 
                _infobox = True, 
                heading = 'No. of Harts', 
                description = 'No. of Harts No. of Harts No. of Harts', 
                numbers_only=True,
                default_fixed=True,
                )

a = createTrueFalse("Overlap Redirections", 
                _infobox = True, 
                heading= 'Overlap Rediretions', 
                description='Overlap Rediretions Overlap Rediretions Overlap Rediretions',
                default_fixed=True,
                fixed_val=True)

createCounterField('No. of Times hit', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?')

createDropDown([' -O3', ' -O2', ' -O1'], 
               'Optimization Type', 
               'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?')

createTextEntry("Text also", 
                fixed_val = '', 
                _infobox = True, 
                heading = 'Hello', 
                description = 'What\'s is up Overlap Rediretions Overlap Rediretions Overlap Rediretions')



run_window()