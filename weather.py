
import json
import urllib

#Get the weather
city="Pune"
url="http://api.openweathermap.org/data/2.5/weather?q="+city
jsonurl = urllib.urlopen(url)
text = json.loads(jsonurl.read())

weather_desc=text["weather"][0]["description"]	# General description of the weather
temp=float(text["main"]["temp"])-273.15			# Temperature in C
pressure=text["main"]["pressure"]				# Pressure in hPa
humidity=text["main"]["humidity"]				# Humidity %
wind_speed=text["wind"]["speed"]				# Wind speed mps
'''
{u'clouds': {u'all': 0}, 
u'name': u'Pune', 
u'coord': {u'lat': 18.52, u'lon': 73.86}, 
u'sys': {u'country': u'IN', u'message': 1.7015, u'sunset': 1430486773, u'sunrise': 1430440627}, 
u'weather': [{u'main': u'Clear', u'id': 800, u'icon': u'01d', u'description': u'Sky is Clear'}], 
u'cod': 200, u'base': u'stations', u'dt': 1430465398, u'main': 
{u'temp': 309.54, u'grnd_level': 953.26, u'temp_max': 309.54, u'sea_level': 1022.72, u'humidity': 31, u'pressure': 953.26, u'temp_min': 309.54}, 
u'id': 1259229, u'wind': {u'speed': 3.22, u'deg': 311.5}}

'''


print text
print 'City : %s\nDesc: %s\nTemp: %s\nPressure: %s\nHumidity: %s%%\nWind Speed: %s' %(city, weather_desc,temp,pressure,humidity,wind_speed)
