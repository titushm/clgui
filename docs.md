# clgui Documentation

## Overview
The `clgui` library allows developers to create command-line GUIs with layouts and interactive elements. It currently supports a vertical stack layout (`VStack`) and interactive elements like `Button` and `ButtonList`.

## Installation
To install the library, use pip:
```
pip install clgui
```

## Navigation
- Use **up** and **down arrow keys** to control the selected element.
- Press **Escape** to enter preview mode, which allows you to switch between different elements in the layout.
- Press **Enter** to interact with selected buttons.

## Usage
Below is an example of how to create a simple GUI using `clgui`:

```python
import clgui

# Create a vertical layout
vertical_layout = clgui.layout.VStack()

# Initialize the GUI
main = clgui.GUI(layout=vertical_layout)

# Create elements
button_list = clgui.ButtonList()
button_list.setTitle("Button List")

# Create buttons with and without handlers
def handleClick(data):
    print(f"Button clicked with data: {data}")

button1 = clgui.Button("Hello", handleClick, ["data1", "data2"])
button2 = clgui.Button("World") 

# Add buttons to the button list
button_list.addButtons([button1, button2])

# Add a standalone button
standalone_button = clgui.Button("I am a button")

# Add elements to the layout
vertical_layout.add(button_list)
vertical_layout.add(standalone_button)

# Show the GUI
main.show()

# When done with the GUI
main.destroy()
```

## Components

### GUI
- The main class to initialize and manage the GUI.
- **Methods**:
  - `show()`: Displays the GUI and starts listening for user input.
  - `destroy()`: Closes the GUI and stops listening for input.

### VStack
- A layout class that stacks elements vertically.
- **Methods**:
  - `add(child)`: Adds a child element to the layout.

### ButtonList
- A container for multiple buttons.
- **Methods**:
  - `setTitle(title)`: Sets the title of the button list.
  - `addButtons(buttons)`: Adds multiple buttons to the list.
  - `addButton(button)`: Adds a single button to the list.

### Button
- Represents a clickable button.
- **Constructor Parameters**:
  - `label`: The text to display on the button.
  - `callback` (optional): Function to call when the button is clicked.
  - `data` (optional): Data to pass to the callback function.

## Event Handling
Buttons can have event handlers that are triggered when the "Enter" key is pressed. For example:

```python
def handleClick(data):
    print(f"Button clicked with data: {data}")

button = clgui.Button("Click me", handleClick, ["example_data"])
```

## License
This library is licensed under the Mozilla Public License Version 2.0 (MPL 2.0).
For more details, refer to the LICENSE file in the repository.