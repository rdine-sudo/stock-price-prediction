from django.contrib import admin
from django.urls import path, include
from backend1app import views

urlpatterns = [
        path('top_gainers/', views.top_gainers.as_view()),
        path('top_losers/', views.top_losers.as_view()),
        path('nifty/', views.nifty.as_view()),
        path('nifty_mid_50/', views.nifty_mid_50.as_view()),
        path('nifty_next_50/', views.nifty_next_50.as_view()),
        path('nifty_auto/', views.nifty_auto.as_view()),
        path('nifty_bank/', views.nifty_bank.as_view()),
        path('nifty_small_cap_50/', views.nifty_small_cap_50.as_view()),
]
