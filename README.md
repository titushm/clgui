# clgui

Command-Line-GUI

# Docs

## Install clgui

`pip install clgui`

## Create new gui

```py
import clgui

vertical_layout = clgui.Layouts.VStack() # Currently the only layout is VStack, more are planned
main = clgui.GUI(layout=vertical_layout) # Initialize a new GUI

# Elements
button_list = clgui.ButtonList() # Currently the only element types are ButtonList and Button, more are planned
button = clgui.Button("click me") # Buttons do not need event handlers but can have them.

def handleClick(data):
	print(data)
# Methods
button1 = clgui.Button("Hello", handleClick, ["data1", "data2"]) # Create a new button with an event handler when enter is pressed on it
button2 = clgui.Button("World", lambda: print("World"), "extra data") # Create a new button with an event handler when enter is pressed on it
button_list.addButtons([button1, button2]) # Add buttons to the button list

button_list.addButton(button1) # A single button can also be added

vertical_layout.add(button_list) # Add button list to the layout
vertical_layout.add(button) # You can also directly add a button to the layout
main.show() # Show the main GUI
main.destroy() # Close the gui
```
