from django.contrib import admin
from django.urls import path, include
from lstmapp import views

urlpatterns = [
        path('top_gainers/', views.top_gainers.as_view()),
        path('forecast/', views.Security_forecast_API.as_view()),
]
