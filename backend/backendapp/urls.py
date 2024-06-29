"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backendapp import views

urlpatterns = [
        path('one/', views.hello_world.as_view()),
        path('list_company/', views.List_company.as_view()),       
        path('prdict_data/', views.predict_data.as_view()),         
        path('hist_data/', views.Hist_data.as_view()),        
        path('hist_data_color/', views.Hist_data_color.as_view()),        
        path('security_name/', views.Security_name.as_view()),
        path('word_cloud/', views.World_cloud.as_view()),        
        # path('news_insert/', views.News_insert,name="news"),      
        path('company_news/', views.Company_News.as_view()),
        path('company_data/', views.Company_data.as_view()),    
        path('company_pos_news/', views.Company_Pos_News.as_view()),  
        path('company_neu_news/', views.Company_Neu_News.as_view()),  
        path('company_neg_news/', views.Company_Neg_News.as_view()),  
        path('company_news_fetch/', views.Company_News_fetch.as_view()),
        path('company_news_fetch_limit/', views.Company_News_fetch_limit.as_view()),  
        path('company_news_sentiment/', views.Company_News_Sentiment.as_view()),  
        path('security_shareholding/', views.Security_Shareholding_API.as_view()),  
        path('security_shareholding_chart/', views.Security_Shareholding_API_Chart.as_view()),  
        path('security_balancesheet/', views.Security_BalanceSheet.as_view()),   
        path('security_quarter_result/', views.Security_Quarter_Result_API.as_view()),  
        path('security_quarter_result_yoy/', views.Security_Quarter_Result_yoy_API.as_view()),  
        path('security_nse_bse_code/', views.List_company_Nse_Bse_code.as_view()),  
        path('user_tool_dropdown/', views.user_tool_dropdown.as_view()),  
        path('user_tool_data/', views.user_tool_data.as_view()),  
        path('security_Top_ratio/', views.Security_Top_ratio.as_view()),  
        path('get-news/', views.get_news, name="news")
        # path('security_balance/', views.Security_Balance_API.as_view()),  

]
