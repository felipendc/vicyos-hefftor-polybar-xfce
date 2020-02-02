#!/bin/python
# -*- coding: utf-8 -*-

# Procedure
# Surf to https://openweathermap.org/city
# Fill in your CITY
# e.g. Antwerp Belgium
# Check url
# https://openweathermap.org/city/2803138
# you will the city code at the end
# create an account on this website
# create an api key (free)
# LANG included thanks to krive001 on discord


import requests

CITY = "3460748"
API_KEY = "756edce7e9d4c385ef9499a53492678c"
UNITS = "Metric"
UNIT_KEY = "C"
#UNIT_KEY = "F"
#LANG = "pt"
LANG = "en"
#LANG = "nl"
#LANG = "hu"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&lang={}&appid={}&units={}".format(CITY, LANG,  API_KEY, UNITS))

try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))

# This is the default setup.
#        print("{}, {} °{}".format(CURRENT, TEMP, UNIT_KEY)) 


# The line below, just show or "print" the weather fetch result in °C without any string. 
# So that, I get more room on the polybar (It's perfect if you own a Laptop).
        print("{} °{}".format(TEMP, UNIT_KEY)) 
    else:
#        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
        print("Error to fetch your CITY CODE, in weather.py") 
        
except (ValueError, IOError):
    print("Error: Unable print the data")
