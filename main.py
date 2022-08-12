from modules.imports import *

frame_1 = createFrame(config.window, side='left', fill='y', pady=(100,0))

createCounterField("No. of Harts",
                    'Arial 11',
                    frame_1,
                _infobox = True, 
                heading = 'No. of Harts', 
                description = '',)

createTrueFalse("Overlap ", 
                    frame_1,
                _infobox = True, 
                heading= 'Overlap Rediretions', 
                description='')

createTrueFalse("Merged RF", 
                    frame_1,
                _infobox = True, 
                heading= 'Overlap Rediretions', 
                description='')

createLabel("ISB Sizes", window_name=frame_1)

frame_2 = createFrame(frame_1, side='top', fill='y', padx=(20, 0))

createCounterField('ISB S0S1', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               window_name=frame_2)

createCounterField('ISB S0S1', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               window_name=frame_2)

createCounterField('ISB S0S1', 
                  'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               window_name=frame_2)

createLabel("S Extension", window_name=frame_1)

createTextEntry('Sfence_d_complexity', fixed_val= 'simple', window_name=frame_1)

createTextEntry('Sfence_i_complexity', fixed_val= 'simple', window_name=frame_1)

createDropDown([' -O3', ' -O2', ' -O1'], 
               'Optimization', 
               'Arial 11',
               _infobox = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?',
               window_name=frame_1)

createTextEntry("Text also", 
                fixed_val = '', 
                _infobox = True, 
                heading = 'Hello', 
                description = 'What\'s is up Overlap Rediretions Overlap Rediretions Overlap Rediretions',
                window_name=frame_1)

run_window()