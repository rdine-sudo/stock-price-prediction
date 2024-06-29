from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response 
from backendapp import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from nsetools import Nse
import yfinance as yf
import json
import pandas as pd
from json import encoder
from backendapp.models import Company_list, Security_Name, Security_News, Security_Balance, Security_ShareHolding , Security_Quarter_Result,Security_Index,Security_Quarter_Result_yoy_data, Security_Name_nse_bse_code,Top_ratios,Security_user_analyse_tool_data
import pandas as pd
from rest_framework import viewsets 
from datetime import date
from nsepy import get_history
from bsedata.bse import BSE as bsedata_bse
b = bsedata_bse()
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
import re
import os
import requests
import time
from django.shortcuts import redirect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from bselib.bse import BSE
from nltk.corpus import stopwords
from pprint import pprint
from nltk.tokenize import word_tokenize
nltk.downloader.download('vader_lexicon')
nltk.downloader.download('punkt')
nltk.downloader.download('stopwords')
b = BSE()

from datetime import date
from nsepy import get_history

# company_det_count = Security_Name.objects.all().count()
# company_det = Security_Name.objects.all()
# i = 0 
# for data in company_det:
#     i =i+1
#     data.id = i
#     data.save()
#     print(data.id)

# nltk.download('vader_lexicon')

# df = pd.read_csv("data_zerodha.csv")
# print(df)
# df_records = df.to_dict('records')
# model_instances = [Security_user_analyse_tool_data(Symbol= record['Symbol'], Trade_Date= record['Trade Date'], Exchange= record['Exchange'], Segment= record['Segment'], Series= record['Series'], Trade_Type= record['Trade Type'], Quantity= record['Quantity'], Price= record['Price'],Trade_ID= record['Trade ID'],Order_ID= record['Order ID'],Order_Execution_Time   = record['Order Execution Time'],dataset_id= record['dataset_id'],user_id= record['user_id'],) for record in df_records]
# obj = Security_user_analyse_tool_data.objects.bulk_create(model_instances)
# print("Done")
# b = BSE()

nse = Nse()


class  hello_world(APIView):
    def get(self,request):
        data1 = One.objects.all()
        serializer1 = serializers.ReactSerializer(data1, many=True)
        return Response(serializer1.data)


def get_news(request):
    if request.method == "GET":
        print("ok")
        comp = request.GET['name']
        response = requests.get('https://news.google.com/search?q='+comp+'&hl=en-IN&gl=IN&ceid=IN%3Aen')
        soup = BeautifulSoup(response.text, 'html.parser') 
        headlines = soup.find_all("a", class_="JtKRv")
        # soup.find_all("a", {"class": "WwrzSb"})
#  soup.find('body').find_all('a') 
        data  = []
        for x in headlines: 
            data.append(x.text.strip())
        print(data)
    return HttpResponse(json.dumps(data),
                    content_type='application/json; charset=utf8')


class List_company(APIView):
    serializer_class = serializers.List_company_ser
    def get(self,request):
        data1 = Company_list.objects.filter(Status="Active",Instrument="Equity")
        serializer1 = serializers.List_company_ser(data1, many=True)
        return Response(serializer1.data)

class List_company_Nse_Bse_code(APIView):
    serializer_class = serializers.List_company_Bse_nse_code
    def get(self,request):
        data1 = Security_Name_nse_bse_code.objects.all()
        serializer1 = serializers.List_company_Bse_nse_code(data1, many=True)
        return Response(serializer1.data)



class Company_data(APIView):
    def get(self,request):
        Company_code = request.GET["name"]
        data1 = Company_list.objects.filter(Status="Active",Security_Code=Company_code)
        print("data ios ,", data1)
        data_dict = {}
        # for data in data1:
        #     Security_Code = data.Security_Code
        #     Issuer_Name =  data.Issuer_Name
        #     Security_Id =  data.Security_Id
        #     Security_Name =  data.Security_Name
        #     Status = data.Status
        #     Group =  data.Group
        #     Face_Value =  data.Face_Value
        #     ISIN_No =  data.ISIN_No
        #     Industry = data.Industry
        #     Instrument =  data.Instrument
        # data_dict = {"Security_Code":Security_Code, "Issuer_Name":Issuer_Name, "Security_Id":Security_Id, "Security_Name":Security_Name, "Status":Status, "Group":Group, "Face_Value":Face_Value, "ISIN_No":ISIN_No, "Industry":Industry, "Instrument":Instrument, }
        return Response(data_dict)

class Company_News(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Name=Company_name)
        serializer1 = serializers.Security_News_ser(data1, many=True)
        return Response(serializer1.data)


class Hist_data(APIView):
    def get(self,request):
        Company_code = request.GET["name"]
        data_company = Security_Name.objects.filter(Security_Code=Company_code)
        for u in data_company:
            print(u.Security_Id)
            Security_Id = u.Security_Id
        df = get_history(symbol=Security_Id,start=date(2021,1,1),end=date.today())
        df['date'] = df.index.astype(str)
        df.index = range(len(df))
        Row_list =[] 
        Row_list.append(['day', 'Close'])
        for index, rows in df.iterrows(): 
            my_list =[rows.date, rows.Close] 
            Row_list.append(my_list) 
        return Response(Row_list)


class Hist_data_color(APIView):
    def get(self,request):
        Company_code = request.GET["name"]
        data_company = Security_Name.objects.filter(Security_Code=Company_code)
        for u in data_company:
            print(u.Security_Id)
            Security_Id = u.Security_Id
        df = get_history(symbol=Security_Id,start=date(2021,1,1),end=date.today())
        first_val = df["High"].iloc[0]
        print(first_val)
        last_val = df["High"].iloc[-1]
        print(last_val)
        if first_val > last_val:
            color_val = "#ff0404"
            color_name = "red"
            type_trend = "Bearish"
            image = "/static/media/bear.803d240b.gif"
            print("#ff0404")
        else:
            color_val = "#46b403"
            color_name = "green"
            type_trend = "Bullish"
            image="/static/media/bull.abda1a38.gif"
            print("#00f623")
        color = {"color":color_val,"color_name":color_name,"type_trend":type_trend,"image":image}
        return Response(color)      

class World_cloud(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Code=Company_name)
        text = ""
        for datas in data1:
            text += " "
            text += datas.Security_News
        print(text)
        text_tokens = word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        def listToString(s):
            str1 = " "
            for ele in s:  
                str1 += " "
                str1 += ele
            return str1  
        string = listToString(tokens_without_sw)

        def freq(str):
            str = str.split()          
            str2 = []
            for i in str:
                if i not in str2:
                    str2.append(i)
            list_count = []
            for i in range(0, len(str2)):
                dict_count = {"text":str2[i],"value":str.count(str2[i])}
                list_count.append(dict_count)
            return list_count
        return Response(freq(string))     

class predict_data(APIView):
    def get(self,request):
        Company_code = request.GET["name"]
        q = b1.getQuote(str(Company_code))
        df = get_history(symbol=q["securityID"],start=date(2015,1,1),end=date.today())
        del df["Symbol"]
        del df["Series"]
        del df["Prev Close"]
        del df["VWAP"]
        del df["Volume"]
        del df["Trades"]
        del df["Turnover"]
        del df["Deliverable Volume"]
        del df["%Deliverble"] 
        df['date'] = df.index.astype(str)
        df.index = range(len(df))
        result = df.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)

class Security_name(APIView):
    def get(self,request):
        data1 = Security_Name.objects.all().order_by('-id')
        serializer1 = serializers.Security_Name_ser(data1, many=True)
        return Response(serializer1.data)

class Company_Pos_News(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Name=Company_name,Sentiment_Overall="success")
        serializer1 = serializers.Security_News_ser(data1, many=True)
        return Response(serializer1.data)



class Company_Neu_News(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Name=Company_name,Sentiment_Overall="info")
        serializer1 = serializers.Security_News_ser(data1, many=True)
        return Response(serializer1.data)


class Company_Neg_News(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Name=Company_name,Sentiment_Overall="danger")
        serializer1 = serializers.Security_News_ser(data1, many=True)
        return Response(serializer1.data)



class Company_News_fetch(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Code=Company_name).order_by('-id')
        serializer1 = serializers.Security_News_ser(data1, many=True)
        return Response(serializer1.data)


class Company_News_fetch_limit(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        data1 = Security_News.objects.filter(Security_Code=Company_name).order_by('-id')[:10]
        serializer1 = serializers.Security_News_ser(data1, many=True)
        return Response(serializer1.data)


class Company_News_Sentiment(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        success_sen = Security_News.objects.filter(Security_Code=Company_name,Sentiment_Overall="success").count()
        info_sen = Security_News.objects.filter(Security_Code=Company_name,Sentiment_Overall="info").count()
        danger_sen = Security_News.objects.filter(Security_Code=Company_name,Sentiment_Overall="danger").count()
        full_count = Security_News.objects.filter(Security_Code=Company_name).count()
        company_det = Company_list.objects.filter(Security_Code=Company_name)
        pos_per = (int(success_sen) * 100 ) / int(full_count)
        neg_per = (int(danger_sen) * 100 ) / int(full_count)
        neu_per = (int(info_sen) * 100 ) / int(full_count)
        print(pos_per)
        print(neg_per)
        print(neu_per)
        # print(full_count)
        res = [["Company_name",Company_name],["Positive",pos_per],["Negative",neg_per],["Neutral",neu_per]]
        # res = {"Company_name":Company_name,"total_news":full_count,"pos":pos_per,"neg":neg_per,"neu":neu_per}
        return Response(res)


class Security_Shareholding_API(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        Company_name = str(Company_name)
        print(Company_name)
        Shareholding_count = Security_ShareHolding.objects.filter(Security_Code=Company_name).count()
        # if Shareholding_count > 0:
        print(Shareholding_count)
        # Shareholding = Security_ShareHolding.objects.filter(Security_Code=Company_name)
        Shareholding = Security_ShareHolding.objects.filter(Security_Code=Company_name)

        print(Shareholding)
        for data in Shareholding:
            Promoters_dec_2020 = data.Promoters_dec_2020
            Promoters_sep_2020 = data.Promoters_sep_2020
            FIIs_dec_2020 = data.FIIs_dec_2020
            FIIs_sep_2020 = data.FIIs_sep_2020
            Mutual_Funds_dec_2020 = data.Mutual_Funds_dec_2020
            Mutual_Funds_sep_2020 = data.Mutual_Funds_sep_2020
            Insurance_Companies_dec_2020 = data.Insurance_Companies_dec_2020
            Insurance_Companies_sep_2020 = data.Insurance_Companies_sep_2020
            Other_DIIs_dec_2020 = data.Other_DIIs_dec_2020
            Other_DIIs_sep_2020 = data.Other_DIIs_sep_2020
            Non_Institution_dec_2020 = data.Non_Institution_dec_2020
            Non_Institution_sep_2020 = data.Non_Institution_sep_2020     
        res = {
                    "Promoters_dec_2020":Promoters_dec_2020,
                    "FIIs_dec_2020":FIIs_dec_2020,
                    "Mutual_Funds_dec_2020":Mutual_Funds_dec_2020,
                    "Insurance_Companies_dec_2020":Insurance_Companies_dec_2020,
                    "Other_DIIs_dec_2020":Other_DIIs_dec_2020,
                    "Non_Institution_dec_2020":Non_Institution_dec_2020,
                    "Promoters_sep_2020":Promoters_sep_2020,
                    "FIIs_sep_2020":FIIs_sep_2020,
                    "Mutual_Funds_sep_2020":Mutual_Funds_sep_2020,
                    "Insurance_Companies_sep_2020":Insurance_Companies_sep_2020,
                    "Other_DIIs_sep_2020":Other_DIIs_sep_2020,
                    "Non_Institution_sep_2020":Non_Institution_sep_2020}
        # else:
        #     res = {
        #                 "Promoters_dec_2020":"NA",
        #                 "FIIs_dec_2020":"NA",
        #                 "Mutual_Funds_dec_2020":"NA",
        #                 "Insurance_Companies_dec_2020":"NA",
        #                 "Other_DIIs_dec_2020":"NA",
        #                 "Non_Institution_dec_2020":"NA",
        #                 "Promoters_sep_2020":"NA",
        #                 "FIIs_sep_2020":"NA",
        #                 "Mutual_Funds_sep_2020":"NA",
        #                 "Insurance_Companies_sep_2020":"NA",
        #                 "Other_DIIs_sep_2020":"NA",
        #                 "Non_Institution_sep_2020":"NA"}

        return Response(res)


class Security_Shareholding_API_Chart(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        Shareholding = Security_ShareHolding.objects.filter(Security_Code=Company_name)
        for data in Shareholding:
            Promoters_dec_2020 = data.Promoters_dec_2020
            Promoters_sep_2020 = data.Promoters_sep_2020
            FIIs_dec_2020 = data.FIIs_dec_2020
            FIIs_sep_2020 = data.FIIs_sep_2020
            Mutual_Funds_dec_2020 = data.Mutual_Funds_dec_2020
            Mutual_Funds_sep_2020 = data.Mutual_Funds_sep_2020
            Insurance_Companies_dec_2020 = data.Insurance_Companies_dec_2020
            Insurance_Companies_sep_2020 = data.Insurance_Companies_sep_2020
            Other_DIIs_dec_2020 = data.Other_DIIs_dec_2020
            Other_DIIs_sep_2020 = data.Other_DIIs_sep_2020
            Non_Institution_dec_2020 = data.Non_Institution_dec_2020
            Non_Institution_sep_2020 = data.Non_Institution_sep_2020     
        res = [
                ['Year', 'Sep 2020','Dec 2020'],
                ['Promoters', float(Promoters_sep_2020),float(Promoters_dec_2020)],
                ['FII',float(FIIs_sep_2020),float(FIIs_dec_2020)],
                ['DII', float(Other_DIIs_sep_2020),float(Other_DIIs_dec_2020)],
                ['Mutual Fund', float(Mutual_Funds_sep_2020),float(Mutual_Funds_dec_2020)],
                ['Insurance', float(Insurance_Companies_sep_2020),float(Insurance_Companies_dec_2020)],
                ['Non Institution',float(Non_Institution_sep_2020),float(Non_Institution_dec_2020)],
            ]
        return Response(res)


class Security_BalanceSheet(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        balance_count = Security_Balance.objects.filter(Security_Code=Company_name).count()
        if balance_count > 0:
                
            balance = Security_Balance.objects.filter(Security_Code=Company_name)
            for data in balance:
                Share_Capital	  = data.Share_Capital
                Reserves     	  = data.Reserves
                Borrowings   	  = data.Borrowings
                Other_Liabilities = data.Other_Liabilities
                Total_Liabilities = data.Total_Liabilities
                Fixed_Assets	  = data.Fixed_Assets
                CWIP        	  = data.CWIP
                Investments 	  = data.Investments
                Other_Assets	  = data.Other_Assets
                Total_Assets	  = data.Total_Assets 
            res = {"Share_Capital" : Share_Capital,"Reserves" : Reserves,"Borrowings" : Borrowings,"Other_Liabilities" : Other_Liabilities,"Total_Liabilities" : Total_Liabilities,"Fixed_Assets" : Fixed_Assets,"CWIP" : CWIP,"Investments" : Investments,"Other_Assets" : Other_Assets,"Total_Assets" : Total_Assets,}
        else:
            res = {"Share_Capital" : "NA","Reserves" : "NA","Borrowings" : "NA","Other_Liabilities" : "NA","Total_Liabilities" : "NA","Fixed_Assets" : "NA","CWIP" : "NA","Investments" : "NA","Other_Assets" : "NA","Total_Assets" : "NA",}
        return Response(res)


class Security_Quarter_Result_API(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        quarter_result_count = Security_Quarter_Result.objects.filter(Security_Code=Company_name).count()
        if quarter_result_count > 0:
            quarter_result = Security_Quarter_Result.objects.filter(Security_Code=Company_name)
            for data in quarter_result:
                Security_Code 			= data.Security_Code
                Security_Name 			= data.Security_Name
                Sales 					= data.Sales
                Expenses				= data.Expenses
                Operating_profit 		= data.Operating_profit
                Opm 					= data.Opm
                Other_income 			= data.Other_income
                Interest 				= data.Interest
                Depreciation			= data.Depreciation
                Profit_before_tax 		= data.Profit_before_tax
                Tax_percentage 			= data.Tax_percentage
                Net_profit 				= data.Net_profit
                Eps 					= data.Eps
                year 					= data.year
            res = {"Security_Code":Security_Code,"Security_Name":Security_Name,"Sales":Sales,"Expenses":Expenses,"Operating_profit":Operating_profit,"Opm":Opm,"Other_income":Other_income,"Interest":Interest,"Depreciation":Depreciation,"Profit_before_tax":Profit_before_tax,"Tax_percentage":Tax_percentage,"Net_profit":Net_profit,"Eps":Eps,"year":year}
        else:
            res = {"Security_Code":"NA","Security_Name":"NA","Sales":"NA","Expenses":"NA","Operating_profit":"NA","Opm":"NA","Other_income":"NA","Interest":"NA","Depreciation":"NA","Profit_before_tax":"NA","Tax_percentage":"NA","Net_profit":"NA","Eps":"NA","year":"NA"}
        return Response(res)


class Security_Quarter_Result_yoy_API(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        quarter_result_count = Security_Quarter_Result_yoy_data.objects.filter(Security_Code=Company_name).count()
        if quarter_result_count > 0:
            quarter_result = Security_Quarter_Result_yoy_data.objects.filter(Security_Code=Company_name)
            for data in quarter_result:
                Security_Code 			= data.Security_Code
                Security_Name 			= data.Security_Name
                Sales 					= data.Sales
                Expenses				= data.Expenses
                Operating_profit 		= data.Operating_profit
                Opm 					= data.Opm
                Other_income 			= data.Other_income
                Interest 				= data.Interest
                Depreciation			= data.Depreciation
                Profit_before_tax 		= data.Profit_before_tax
                Tax_percentage 			= data.Tax_percentage
                Net_profit 				= data.Net_profit
                Eps 					= data.Eps
                year 					= data.year
            res = {"Security_Code":Security_Code,"Security_Name":Security_Name,"Sales":Sales,"Expenses":Expenses,"Operating_profit":Operating_profit,"Opm":Opm,"Other_income":Other_income,"Interest":Interest,"Depreciation":Depreciation,"Profit_before_tax":Profit_before_tax,"Tax_percentage":Tax_percentage,"Net_profit":Net_profit,"Eps":Eps,"year":year}
        else:
            res = {"Security_Code":"NA","Security_Name":"NA","Sales":"NA","Expenses":"NA","Operating_profit":"NA","Opm":"NA","Other_income":"NA","Interest":"NA","Depreciation":"NA","Profit_before_tax":"NA","Tax_percentage":"NA","Net_profit":"NA","Eps":"NA","year":"NA"}
        return Response(res)
        
class Security_Top_ratio(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        Top_ratios_data = Top_ratios.objects.filter(Security_Code=Company_name)
        for data in Top_ratios_data:
            Security_Code =data.Security_Code
            Security_Name =data.Security_Name
            Security_Id =data.Security_Id
            Market_Cap = data.Market_Cap
            Current_Price = data.Current_Price
            High= data.High
            Low = data.Low
            Stock_PE =data.Stock_PE
            Book_Value = data.Book_Value
            Dividend_Yield = data.Dividend_Yield
            ROCE = data.ROCE
            ROE =  data.ROE
            Face_Value =data.Face_Value
            About =data.About
        res = {"Security_Code":Security_Code,"Security_Name":Security_Name,"Security_Id" :Security_Id ,"Market_Cap" :Market_Cap  ,"Current_Price":Current_Price,"High":High,"Low":Low ,"Stock_PE":Stock_PE,"Book_Value":Book_Value, "Dividend_Yield":Dividend_Yield, "ROCE":ROCE, "ROE":ROE ,"Face_Value":Face_Value, "About":About}
        return Response(res)

class user_tool_dropdown(APIView):
    def get(self,request):
        quarter_result_count = Security_user_analyse_tool_data.objects.all()
        sec_id_list = []
        for i in quarter_result_count:
            sec_id_list.append(i.Symbol)
        with_out_duplicate= []

        for i in sec_id_list: 
            if i not in with_out_duplicate: 
                with_out_duplicate.append(i)
        with_dict = []
        for i in with_out_duplicate:
            with_dict.append({"Symbol":i})
        return Response(with_dict)





class user_tool_data(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        hist = get_history(symbol='BHEL', start=date(2021,2,2), end=date.today())
        current = float(hist.tail(1)["Last"])
        data_tool = Security_user_analyse_tool_data.objects.filter(Symbol=Company_name)
        list_out = [["Date","Buy","Current Price"]]
        for data in data_tool:
            if data.Trade_Type == "sell":
                list_in = [data.Trade_Date,float(data.Price),float(current)]
                list_out.append(list_in)
            # else:
            #     list_in = [data.Trade_Date,float(data.Price),float(current)]
            #     list_out.append(list_in)
        return Response(list_out)





# def News_insert(): 
#     company_det = Security_Name_nse_bse_code.objects.all().order_by("-id")[0:100]
#     count = 0 
#     for i in company_det:
#         count = count + 1
#         print("\n \n ")
#         company_name = i.Security_Name
#         company_code = i.Security_Code
#         print(count , " -- " ,company_name)
#         print("\n \n ")
#         url_all_single = "https://news.google.com/search?q={} share price &hl=en-IN&gl=IN&ceid=IN%3Aen".format(company_name)
#         req_all_single = requests.get(url_all_single,)
#         soup = BeautifulSoup(req_all_single.content, 'html.parser')
#         datas_all_single = []
#         sid_obj = SentimentIntensityAnalyzer()
#         for str2 in soup.findAll("h3"):
#             news = str2.text.strip('\t\r\n')
#             sentiment_dict = sid_obj.polarity_scores(news)
#             Sentiment_Overall_var = ""
#             if sentiment_dict['compound'] >= 0.05 : 
#                 Sentiment_Overall_var = "success"
#             elif sentiment_dict['compound'] <= - 0.05 : 
#                 Sentiment_Overall_var = "danger"
#             else : 
#                 Sentiment_Overall_var = "info"
#             data_news = Security_News.objects.create(Security_Code=company_code,Security_Name=company_name,Security_News=news,Sentiment_Pos=sentiment_dict['pos']*100,Sentiment_Neg=sentiment_dict['neg']*100,Sentiment_Neu=sentiment_dict['neu']*100,Sentiment_Com=sentiment_dict['compound'],Sentiment_Overall=Sentiment_Overall_var)
#             data_news.save() 
#             print(news)
#         time.sleep(4)
#     data1 = Security_Name.objects.all()
#     context = {"name":data1}
# News_insert()

# def top_ratios():
#     data1 = Security_Name_nse_bse_code.objects.all().order_by('-id')[0:100]

#     count = 0
#     for i in data1:
#         # print(i)
#         count = count + 1
#         id_data = i.Security_Id
#         url_all_single = "https://www.screener.in/company/"+str(i.Security_Code)
#         req_all_single = requests.get(url_all_single,)
#         soup = BeautifulSoup(req_all_single.content, 'html.parser')
#         datas_all_single1 = []
#         for str2 in soup.findAll("ul", {"id": "top-ratios"}):
#             for str1 in str2.findAll("span",{"class":"number"}):
#                 datas_all_single1.append(str1.text.strip('\t\r\n'))
#         for str2 in soup.findAll("div", {"class": "company-profile"}):
#             for str1 in str2.findAll("p"):
#                 if str1:
#                     datas_all_single1.append(str1.text.strip('\t\r\n'))
#                 else:
#                     datas_all_single1.append("NA")
#         print(count , " - -- -",  i.Security_Name ," - ",datas_all_single1,)
#         print((datas_all_single1)) 
#         if len(datas_all_single1) == 10:
#             data_index = Top_ratios.objects.create(Security_Code = i.Security_Code, Security_Name = i.Security_Name, Security_Id = i.Security_Id, Market_Cap = datas_all_single1[0], Current_Price =  datas_all_single1[1], High=  datas_all_single1[2], Low =  datas_all_single1[3], Stock_PE =  datas_all_single1[4], Book_Value =  datas_all_single1[5], Dividend_Yield =  datas_all_single1[6], ROCE =  datas_all_single1[7], ROE = datas_all_single1[8],Face_Value =  datas_all_single1[9], About = "NA")
#             data_index.save()
#         else:
#             data_index = Top_ratios.objects.create(Security_Code = i.Security_Code, Security_Name = i.Security_Name, Security_Id = i.Security_Id, Market_Cap = datas_all_single1[0], Current_Price =  datas_all_single1[1], High=  datas_all_single1[2], Low =  datas_all_single1[3], Stock_PE =  datas_all_single1[4], Book_Value =  datas_all_single1[5], Dividend_Yield =  datas_all_single1[6], ROCE =  datas_all_single1[7], ROE = datas_all_single1[8],Face_Value =  datas_all_single1[9], About = datas_all_single1[10],)
#             data_index.save()
#         print("\n \n")
#         time.sleep(15)
# top_ratios()

# class Security_Balance_API(APIView):
#     def get(self,request):
#         Company_name = request.GET["name"]
#         Balance = Security_Balance.objects.filter(Security_Code=Company_name)
#         for data in Balance:
#             Share_Capital = data.Share_Capital
#             Reserves      = data.Reserves
#             Borrowings    = data.Borrowings
#             Other_Liabilities = data.Other_Liabilities
#             Total_Liabilities = data.Total_Liabilities
#             Fixed_Assets = data.Fixed_Assets
#             CWIP         = data.CWIP
#             Investments  = data.Investments
#             Other_Assets = data.Other_Assets
#             Total_Assets = data.Total_Assets
#         res = { "Share_Capital":Share_Capital,
#                 "Reserves":Reserves,
#                 "Borrowings":Borrowings,
#                 "Other_Liabilities":Other_Liabilities,
#                 "Total_Liabilities":Total_Liabilities,
#                 "Fixed_Assets":Fixed_Assets,
#                 "CWIP":CWIP,
#                 "Investments":Investments,
#                 "Other_Assets":Other_Assets,
#                 "Total_Assets":Total_Assets,
#         }
#         return Response(res)

# def balance_sheet():
#     company_det = Security_Name_nse_bse_code.objects.all().order_by('-id')[0:100]
#     count = 0 
#     for i in company_det:
#         print("\n \n ")
#         count = count + 1
#         company_name = i.Security_Name
#         company_code = i.Security_Code
#         print(company_code)
#         print("\n \n ")
#         fin = b.statement(company_code,stats="balancesheet")
#         if "info" in fin:
#             print(count, " - ",company_code," : Not Founded : ",company_name)
#             pass
#         else:
#             data_balance = Security_Balance.objects.create(Security_Code = company_code, Security_Name = company_name , Share_Capital = fin["share_capital"], Reserves = fin["reserves"], Borrowings = fin["borrowings"], Other_Liabilities = fin["other_liabilities"], Total_Liabilities = fin["total_liabilities"], Fixed_Assets= fin["fixed_assets"], CWIP = fin["CWIP"], Investments = fin["investments"], Other_Assets= fin["other_assets"], Total_Assets = fin["total_assets"])
#             data_balance.save()
#             print(count, " - ",company_code," : Balance Sheet Founded : " , company_name)

#         time.sleep(5)
# balance_sheet()

# def Security_ShareHolding_function():
#     company_det = Security_Name_nse_bse_code.objects.all().order_by('-id')[0:100]
#     count = 0 
#     for i in company_det:
#         print("\n \n ")
#         count = count + 1
#         company_name = i.Security_Name
#         company_code = i.Security_Code
#         print(company_code)
#         print("\n \n ")
#         data = b.holdings(str(company_code))
#         data =  data["holding_comp"]["data"]
#         if "info" in data:
#             print(count, " - ",company_code," : Not Founded : ",company_name)
#             pass
#         else:
#             Promoters_dec_2020 = data[1][1]
#             Promoters_sep_2020 = data[1][2]
#             FIIs_dec_2020 = data[2][1]
#             FIIs_sep_2020 = data[2][2]
#             Mutual_Funds_dec_2020 = data[3][1]
#             Mutual_Funds_sep_2020 = data[3][2]
#             Insurance_Companies_dec_2020 = data[4][1]
#             Insurance_Companies_sep_2020 = data[4][2]
#             Other_DIIs_dec_2020 = data[5][1]
#             Other_DIIs_sep_2020 = data[5][2]
#             Non_Institution_dec_2020 = data[6][1]
#             Non_Institution_sep_2020 = data[6][2]
#             data_balance = Security_ShareHolding.objects.create(Security_Code = company_code,Security_Name = company_name,Promoters_dec_2020 = Promoters_dec_2020,Promoters_sep_2020 = Promoters_sep_2020,FIIs_dec_2020 = FIIs_dec_2020,FIIs_sep_2020 = FIIs_sep_2020,Mutual_Funds_dec_2020 = Mutual_Funds_dec_2020,Mutual_Funds_sep_2020 = Mutual_Funds_sep_2020,Insurance_Companies_dec_2020 = Insurance_Companies_dec_2020,Insurance_Companies_sep_2020 = Insurance_Companies_sep_2020,Other_DIIs_dec_2020 = Other_DIIs_dec_2020,Other_DIIs_sep_2020 = Other_DIIs_sep_2020,Non_Institution_dec_2020 = Non_Institution_dec_2020,Non_Institution_sep_2020 = Non_Institution_sep_2020)
#             data_balance.save()
#             print(count, " - ",company_code," : Share Holding Pattern is  Founded : " , company_name)
#         time.sleep(3)
# Security_ShareHolding_function()


# def Security_Quarter_Results_function():
#     company_det = Security_Name_nse_bse_code.objects.all().order_by('-id')[0:100]
#     count = 0 
#     for i in company_det:
#         print("\n \n ")
#         count = count + 1
#         company_name = i.Security_Name
#         company_code = i.Security_Code
#         print("\n \n ")
#         qty_res = b.statement(company_code,stats="quarter_results")
#         if "info" in qty_res:
#             print(count, " - ",company_code," : Not Founded : ",company_name)
#             pass
#         else:
#             data_balance = Security_Quarter_Result.objects.create(Security_Code = company_code, Security_Name = company_name, Sales = qty_res["sales"], Expenses = qty_res["expenses"], Operating_profit = qty_res["operating_profit"], Opm = qty_res["opm"], Other_income = qty_res["other_income"], Interest = qty_res["interest"], Depreciation = qty_res["depreciation"], Profit_before_tax = qty_res["profit_before_tax"], Tax_percentage = qty_res["tax_percentage"], Net_profit = qty_res["net_profit"], Eps = qty_res["eps"])
#             data_balance.save()
#             print(count, " - ",company_code," : Quterly Result is   Founded : " , company_name)
#         time.sleep(2)
# Security_Quarter_Results_function()

# from nsetools import Nse
# nse1 = Nse()

# def Security_Index_Insert():
#     count = 0
#     nse_index_list = nse1.get_index_list()
#     for i in nse_index_list:
#         count = count + 1
#         data_index = Security_Index.objects.create(Security_exchange="NSE" , Security_index_name=i)
#         data_index.save()
#         print(count, " - ",i," -  is   Added in Database" )

# Security_Index_Insert()


# def Security_Quarter_Results_function_update_year():
#     company_det_count = Security_Quarter_Result.objects.all().count()
#     for i in range(1,company_det_count):
#         company_det = Security_Quarter_Result.objects.filter(id=i).update(year='2023')
#     print("Ok")
# Security_Quarter_Results_function_update_year()



# def Security_Quarter_Results_function_yoy():
#     company_det = Security_Name_nse_bse_code.objects.all().order_by('-id')[0:100]
#     count = 0 
#     for i in company_det:
#         print("\n \n ")
#         count = count + 1
#         company_name = i.Security_Name
#         company_code = i.Security_Code
#         print("\n \n ")
#         qty_res = b.statement(company_code,stats="yoy_results")
#         if "info" in qty_res:
#             print(count, " - ",company_code," : Not Founded : ",company_name)
#             pass
#         else:
#             data_balance = Security_Quarter_Result_yoy_data.objects.create(Security_Code = company_code, Security_Name = company_name, Sales = qty_res["sales"], Expenses = qty_res["expenses"], Operating_profit = qty_res["operating_profit"], Opm = qty_res["opm"], Other_income = qty_res["other_income"], Interest = qty_res["interest"], Depreciation = qty_res["depreciation"], Profit_before_tax = qty_res["profit_before_tax"], Tax_percentage = qty_res["tax_percentage"], Net_profit = qty_res["net_profit"], Eps = qty_res["eps"],year="2020")
#             data_balance.save()
#             print(count, " - ",company_code," : Quterly Result is   Founded : " , company_name)
#         time.sleep(2)
# Security_Quarter_Results_function_yoy()



