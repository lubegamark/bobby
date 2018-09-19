from django.urls import path

from . import views

urlpatterns = [
    path('<symbol>/', views.get_stock),
]
