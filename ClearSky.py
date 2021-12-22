'''
ClearSky
Version 1
Created by Marissa Klein, Wellesley College 2022
Intended use is getting evening forecast for the next week
'''
import requests 
import json
from geopy.geocoders import Nominatim

class ClearSky:
    
    def __init__(self):
        pass
    
    def locationGet(self,loc):
        '''
        Gets latitude and longitude of a specific location.
        args:
            loc(str) must be a valid city and state/country
        raises:
            none
        returns:
            latitude and longitude as a tuple
        '''
        self.loc = loc
        app = Nominatim(user_agent="ClearSky")
        location = app.geocode(loc).raw
        latitude = location['lat']
        longitude = location['lon']
        location = (latitude, longitude)
        return location
    
    def URLRet(self,loc):
        '''
        Retrieves proper NWS API URL.
        args:
            loc(str) must be a valid city and state/country
        raises:
            none
        returns:
            NWS weather JSON data for a specific location
        '''
        self.loc = loc
        coords = self.locationGet(loc)
        lat = coords[0]
        long = coords[1]
        
        #First API Call
        response = requests.get('https://api.weather.gov/points/'+lat+','+long)
        json_data = json.loads(response.text)
        
        #Second API Call
        url = json_data['properties']['forecast']
        forecast = requests.get(url)
        forecast_data = json.loads(forecast.text)
        
        return forecast_data
        
    def getForecast(self,loc):
        '''
        Gets forecast for the next week's evenings.
        args:
            loc(str) must be a valid city and state/country
        raises:
            none
        returns:
            Detailed forecast of the next seven nights.
        '''
        self.loc = loc
        forecast = self.URLRet(loc)
        
        nights = []
        nightFor = []
        data_len=len(forecast['properties']['periods'])
        
        #Finds the data for nights only
        for x in range(data_len):
            keyWord = forecast['properties']['periods'][x]['name']
            checkOne = keyWord.find('night')
            checkTwo = keyWord.find('Night')
            
            if checkOne == -1 and checkTwo == -1:
                pass
            
            else:
                nights.append(x)
        
        #Pulls the detailed forecast for the identified entries              
        for x in nights:
            name = forecast['properties']['periods'][x]['name']
            nightSky = name+": "+forecast['properties']['periods'][x]['detailedForecast']
            nightFor.append(nightSky)
        
        #Prints forecast
        print(*nightFor, sep = '\n\n')
        
        
