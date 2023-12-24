import clgui

vertical_layout = clgui.Layouts.VStack()
main = clgui.GUI(layout=vertical_layout)
button_list = clgui.ButtonList()
button1 = clgui.Button("Hello", lambda: print("Hello"))
button2 = clgui.Button("World", lambda: print("World"))
button_list.addButtons([button1, button2])

vertical_layout.add(button_list)
main.show()