# weatherService.py

import requests

class WeatherService:
    baseUrl= 'https://api.openweathermap.org/data/2.5/forecast' #?q={city name},{state code},{country code}&appid={API key}
    appId = 'da2a287a5155d9a4647f5382a7f8ff85'

    @classmethod
    def getForecast(cls, city = 'new york', country = 'us'):

        response = requests.get(cls.baseUrl, params=[
            ('appid', cls.appId),
            ('q', f'{city}, {country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
        ])

        data = response.json()

        return data['list']

if __name__ == "__main__":
    print(WeatherService.getForecast())