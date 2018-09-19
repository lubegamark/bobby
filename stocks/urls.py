from django.urls import path

from . import views

urlpatterns = [
    path('stocks/<symbol>/', views.get_stock),
    path('weather/<town>/', views.get_weather),
]
