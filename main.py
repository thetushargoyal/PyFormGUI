from modules.imports import *

frame_1 = createFrame(config.window, side='left', fill = 'y', padx=(10, 0), pady=(10, 0))

num_harts_description = 'Description: Total number of harts to be instantiated in the dummy test-soc. Note that these will non-coherent cores simply acting as masters on the fast-bus.'

createTextEntry(frame_1, 
                'num_harts', 
                infoboxBool = True, 
                heading='num_harts', 
                description=num_harts_description, 
                numbers_only=True)

createTrueFalse(frame_1,
                "Overlap", 
                infoboxBool = True, 
                heading= 'Overlap Rediretions', 
                description='')

createLabel(frame_1, "ISB Sizes")

frame_2 = createFrame(frame_1, side='top', padx=(20, 0))

createCounterField(frame_2,
                'ISB S0S1', 
               infoboxBool = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?')

createTextEntry(frame_2, 'Sfence_d_complexity', default_val= 'simple')

createDropDown(frame_1,
               ['-O3', '-O2', '-O1'], 
               'Optimization', 
               infoboxBool = True,
               heading= 'Optimization',
               description= 'Hello Mister how do you do?')

window_1 = createWindow(frame_1)

frame_1_1 = createFrame(window_1, padx=(20, 20), pady=(20, 20))

createCounterField(frame_1_1,
                    "No. of Harts",
                    infoboxBool = True, 
                    heading = 'No. of Harts', 
                    description = '',)

window_1_1 = createWindow(frame_1_1, 'Ways')

createCounterField(window_1_1,
                "No. of Harts",
                infoboxBool = True, 
                heading = 'No. of Harts', 
                description = '',)

run_window()