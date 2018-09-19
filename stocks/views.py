import requests
from django.http import HttpResponse
from django.conf import settings

def get_stock(request, symbol):
    BASE_URL = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_DAILY'
    api_key = settings.ALPHA_ADVANTAGE_API_KEY
    url = '{}?function={}&symbol={}&apikey={}'.format(
        BASE_URL,
        function,
        symbol,
        api_key)

    r = requests.get(url=url)

    html = "<html><body>The data is <br/>{}.</body></html>".format(r.json())
    return HttpResponse(html)

def get_weather(request, town):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = settings.ALPHA_ADVANTAGE_API_KEY
    url = '{}?q={}&APPID={}'.format(
        BASE_URL,
        town,
        api_key)

    r = requests.get(url=url)

    html = "<html><body>The data is <br/>{}.</body></html>".format(r.json())
    return HttpResponse(html)