from modules.imports import *

top_line_label = tk.Label(window, 
                          text="Configure Your Chromite Core", 
                          font= "Arial 15 bold").place(
                          relx = 0.5, 
                          rely =0.03, 
                          anchor = CENTER)

createCounterField("No. of Harts",
                    'Arial 11',
                _infobox = True, 
                heading = 'No. of Harts', 
                description = '',
                )

a = createTrueFalse("Overlap Redirections", 
                _infobox = True, 
                heading= 'Overlap Rediretions', 
                description='',)

b = createTrueFalse("Merged RF", 
                _infobox = True, 
                heading= 'Overlap Rediretions', 
                description='')

createLabel("ISB Sizes")

createCounterField('ISB S0S1', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               setoff= 20)

createCounterField('ISB S1S2', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               setoff= 20)

createCounterField('ISB S2S3', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               setoff= 20)

createCounterField('ISB S3S4', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               setoff= 20)

createCounterField('ISB S4S5', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               setoff= 20)

createCounterField('ISB Cachebuffer', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               setoff= 20)

createLabel("S Extension")

createTextEntry('Sfence_d_complexity', setoff= 20, fixed_val= 'simple')
createTextEntry('Sfence_i_complexity', setoff= 20, fixed_val= 'simple')

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