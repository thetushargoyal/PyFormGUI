# PyFormGUI

## Introduction

Tkinter Tk/Tcl is a cross-platform widget tool kit that is used to create graphical user interfaces (GUIs) for Python programs. Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.

PyFormGUI is a Python module that provides a simple interface to Tkinter. It is designed to be easy to use and to provide a powerful set of widgets that are commonly needed in GUI applications. It is a wrapper around the tkinter module. For more information on tkinter, see the official Python documentation. There are different implementations of how differnet functions are implemented on different platforms. PyFormGUI is designed to work on all platforms.

This project was created for making simple forms using built-in Python Tkinter Library that can fetch values and can be used directly within the program with just a single line required for making a field. (Just like Flutter)

The function has various attributes which can make it read-only, number-only etc. (explained below)

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

Example:

```
main_window = Window.start_window(title = 'PyFormGUI', 
                                  windowIcon = 'info_icon.png', 
                                  fullScreen = False, 
                                  resizable = True)

Window.close_window(main_window)
```

This will create the following window i.e. not fullscreen and resizable.

<p align="center">
  <img width="345" height="290" src="https://user-images.githubusercontent.com/92171383/192292074-0d5551c5-dd28-401f-bac8-8f5cb0fda6f9.png">
</p>

