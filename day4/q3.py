import requests
def weather_details(city , api_key):    
    url="https://api.openweathermap.org/data/2.5/weather?" 
    final_url = f"{url}q={city}&appid={api_key}&units=metric"    
    try:
        response=requests.get(final_url)
        response.raise_for_status()
        data = response.json()
        
        temperature = data["main"]["temp"]  
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]

        print(f"weather in {city} is {data['weather'][0]['description']}")
        print(f"temperature is {temperature} degree celsius")
        print(f"humidity is {humidity}%")
    except requests.exceptions.RequestException as  e:
        print(f"error fetching weather data:{e}")

api_key ="c886a6625554e8c0656caa021caa2de5"
city = input("enter the city name:")

weather_details(city , api_key)