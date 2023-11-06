import PySimpleGUI as sg
import calendar
from datetime import datetime

sg.theme('DarkGrey9')

now = datetime.now()
month = now.month
year = now.year

layout = [
    [sg.Text('Current year and month:')],
    [sg.Output(size=(20,10), key='-OUTPUT-')],
    [sg.Button('Show calendar')]
]

window = sg.Window('Calendar', layout, icon='icon.ico')

while True:
    event, values = window.read()
    if event in (None, 'Выход'):
        break
    if event == 'Show calendar':
        cal = calendar.month(year, month)
        window['-OUTPUT-'].update(cal)

window.close()

