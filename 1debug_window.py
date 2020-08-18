import PySimpleGUI as PSG
# Create some elements
layout = [[PSG.Text("What's your name?"), PSG.InputText()],
          [PSG.Button('OK'), PSG.Button('Cancel')]]
# Create the Window
window = PSG.Window('Hello PySimpleGUI', layout)
# Create the event loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    PSG.Print(f'Event: {event}')
    PSG.Print(str(values))
window.close()