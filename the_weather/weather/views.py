from the_weather.weather.forms import CityForm
from django.shortcuts import render
import requests
from .models import City
def index(request):
    cities = City.objects.all() #return all the cities in the database
    
    url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25 '

    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() 
    
    if request.method == 'POST': #submits only form
        form = CityForm(request.POST) # add request data to form to be processed
        form.save() # validate and save if valid


    form = CityForm()
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request API data to convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add data for current city into thelist
        
        
    context = {'weather_data' : weather_data, 'form' : form}



    return render(request, 'weather/index.html') #returns index.html template
