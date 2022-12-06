This is a classroom excersize where we are using the requests library to perform a GET request from the Open Weather API. 


We'll be consuming the Open Weather API to download realtime weather data in our application.

Before continuing make sure you:

Create an account on https://home.openweathermap.org
Make note of your API key at https://home.openweathermap.org/api_keys

First, we need to install requests:


`pip install requests`

Next, we can complete the WeatherService.getForecast method in the weatherService.py file (top right).

Your tasks are:

Define the baseurl ('https://api.openweathermap.org/data/2.5/forecast') and appId (from the previous step)
Use the requests.get method to call the URL, providing the following query params:
The query (q, f'{city},{country}')
The mode ('mode', 'json')
The appId ('APPID', appId)
Parse the response using response.json() and provide the data in the list key from this response body. The method should return this data.

Lastly we complete the umbrella.py file to make a decision if we'll need an umbrella in a specific city.

The tasks:

1. Fetch data from the API using your WeatherService.getForecast method.
2. Filter this data to only include information for the next 12 hours.
3. Determine if there is a high probability of rain in the remaining data.
4. Return True or False to answer the question of whether we need an umbrella. Print a helpful message based on this result.
5. Practice using the argparse module to dynamically ask a user for a city and country.
Tip: It might be helpful to use an online JSON Parser to help you to navigate the provided JSON data.