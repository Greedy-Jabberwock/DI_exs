from pyowm.owm import OWM
from datetime import timedelta

API_KEY = 'ca169fe72eb955d7f6efcb2173c01670'

owm = OWM(API_KEY)
wtr = owm.weather_manager()
city = 'London'
observation = wtr.weather_at_id(2643743)
weather = observation.weather
wind_dict = weather.wind()
sunrise = weather.sunrise_time("date") + timedelta(hours=3)
sunset = weather.sunset_time('date') + timedelta(hours=3)

print(f'Weather info in {city}')
print(f'Weather: {observation.weather.detailed_status}')
print(f"Wind: {wind_dict['speed']} mps")
print(f'Sunrise: {sunrise.strftime("%H:%M")}')
print(f'Sunset: {sunset.strftime("%H:%M")}')
