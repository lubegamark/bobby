import requests
import datetime
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render

def get_stock(symbol):
    BASE_URL = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_DAILY'
    api_key = settings.ALPHA_ADVANTAGE_API_KEY
    url = '{}?function={}&symbol={}&apikey={}'.format(
        BASE_URL,
        function,
        symbol,
        api_key)

    r = requests.get(url=url)

    return r.json()


def get_weather(town):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = settings.OPEN_WEATHER_API_KEY
    url = '{}?q={}&APPID={}'.format(
        BASE_URL,
        town,
        api_key)

    r = requests.get(url=url)

    return r.json()

def index(request):
    context = {}
    if request.method == 'POST':
        stock = get_stock(request.POST['symbol'])
        symbol = request.POST['symbol']
        city = get_weather(request.POST['city'])
        currency = request.POST['currency']
        print(stock['Time Series (Daily)'][datetime.datetime.now().strftime("%Y-%m-%d")])
        context = {
            "stock": {
                "price": stock['Time Series (Daily)'][datetime.datetime.now().strftime("%Y-%m-%d")]['1. open'],
                "symbol": symbol,
                "high": stock['Time Series (Daily)'][datetime.datetime.now().strftime("%Y-%m-%d")]['2. high'],
                "low": stock['Time Series (Daily)'][datetime.datetime.now().strftime("%Y-%m-%d")]['3. low']
                },
            "weather": {
                "city": city,
                "temperature": city,
            },
            "currency": {
                "currency": currency,
                "price": currency
                }
        }
    return render(request, 'stocks/index.html', context)
