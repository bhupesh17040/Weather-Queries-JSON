# HOMEWORK ASSIGNMENT 1

from urllib.request import *
import datetime


# function to get weather response
def weather_response(location, API_KEY):
        url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + location +'&APPID=' + API_KEY 
        a = urlopen(url)
        json = str(a.read())
        return json