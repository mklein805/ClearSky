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
    [sg.Text('Enter your Location',font=('Helvetica',25)), sg.InputText()],
    [sg.Text('', key = '-TEXT-')],
    [sg.Submit(),sg.Exit()]
    ]

window = sg.Window('ClearSky',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    else:
        loc = values[0]
        
        #Gets the forecast
        sky = ClearSky()
        weather = sky.getForecast(loc)
        forecast = "\n\n".join(weather)
        window['-TEXT-'].update(forecast)

window.close()
        
    
    



'''
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
sg.popup(forecast, title = 'Forecast for '+loc)
'''