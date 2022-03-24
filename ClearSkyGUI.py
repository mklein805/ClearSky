'''
ClearSky GUI
Allows the use of ClearSky with a GUI
Marissa Klein
Wellesley College '22'
'''
import PySimpleGUI as sg
from ClearSky import ClearSky

#Creating first window layout
sg.theme('DarkBlue15')

layout = [
    [sg.Text('Enter your Location'), sg.InputText()],
    [sg.Submit(),sg.Cancel()]
    ]

window = sg.Window('ClearSky', layout)
event, values = window.read()
window.close()

#Read window data
loc = values[0]

#Gets the forecast
sky = ClearSky()
weather = sky.getForecast(loc)
forecast = "\n\n".join(weather)

#Displays forecast
sg.popup(forecast)