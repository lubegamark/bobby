import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_stock(request, symbol):
    BASE_URL = 'https://www.alphavantage.co/query'
    function = 'TIME_SERIES_DAILY'
    api_key = 'demo'
    url = '{}?function={}&symbol={}&apikey={}'.format(
        BASE_URL,
        function,
        symbol,
        api_key)

    r = requests.get(url=url)

    html = "<html><body>The data is <br/>{}.</body></html>".format(r.json())
    return HttpResponse(html)