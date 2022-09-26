# PyFormGUI

## Introduction

This project was created for making simple forms using built-in Python Tkinter Library that can fetch values and can be used directly within the program with just a single line required for making a field. (Just like Flutter)

The function has various attributes which can make it read-only, number-only etc. 

Run main.py for the GUI

## Create an instance of the main window

At the start of your program, call the following function to start the window from the inbuilt Window 

```
main_window = Window.start_window('')
```

This will take the following arguements:

1) title (String): Title of the window 
2) windowIcon (String): Icon of the window  - store your assets in assets folder and pass the name of the image as a string. Eg. 'icon.png'
3) fullscreen (Boolean) - True or False - Default is False, if True, the window will be fullscreen
4) resizable (Boolean) - True or False - Default is True, if False, the window will not be resizable

At the end of your program, call the following function to close the window:

```
Window.close_window(main_window)
```
