import PySimpleGUI as PSG
PSG.SetOptions(
    background_color = "salmon",
    text_element_background_color = "plum",
    text_color = "white"
)

LAYOUT = [ [PSG.Text("Some Text Here")] ]
FORM = PSG.FlexForm("")
FORM.Layout(LAYOUT)

button, value = FORM.Read()