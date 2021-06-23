import requests

from datetime import datetime

api_key = 'be0077544091cb4bfe9d0c2767d65513'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=be0077544091cb4bfe9d0c2767d65513"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#Fetch data (json)
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#file is opened in write mode
f = open("output.txt", "w")
f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time)) 
f.write("\n")
f. write("Current temperature is: {:.2f} deg C".format(temp_city))
f.write("\n") 
f. write ("Current weather desc  :")
f. write (weather_desc)
f.write("\n")
f. write  ("Current Humidity      :")
f. write  (str(hmdt))
f.write("\n")
f.write("Wind speed :")
f.write("{}".format(wind_spd))
f.write('kmph')
f.close()

#open and read the file
f = open("wthrop.txt", "r")
print(f.read())

