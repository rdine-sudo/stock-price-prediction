from django.shortcuts import render 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from nsetools import Nse
import yfinance as yf
import json
from json import encoder
from lstmapp.models import Security_Name,Security_Name1, Security_Forecast
import yfinance as yf 
from datetime import timedelta, date
from datetime import date
from nsepy import get_history
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
import os
import datetime

# df = pd.read_csv("nse_stock_with_bse_code.csv")
# print(df)
# df_records = df.to_dict('records')
# model_instances = [Security_Name(Security_Code=record['Security_Code'],Security_Id=record['Security_Id'] , Security_Name=record['Security_Name'],) for record in df_records]
# obj = Security_Name.objects.bulk_create(model_instances)
# print("Done")


# df = pd.read_csv("nse_stock_with_bse_code.csv")
# print(df)
# df_records = df.to_dict('records')
# model_instances = [Security_Name(Security_Code="",Security_Id=record['Security_Id'],Security_Name=record['Security_Code']) for record in df_records]
# obj = Security_Name.objects.bulk_create(model_instances)
# print("Done")


nse = Nse()


def sec():
    data  = Security_Name.objects.all()[8:100]
    for sec_data in data:
        sec_code = sec_data.Security_Code
        print("sec_data", sec_code)
        print(sec_code)
        json_path = 'http://localhost:8005/hist/?name='+sec_code
        df = pd.read_json(json_path)
        def prepare_data(timeseries_data, n_features):
            X, y =[],[]
            for i in range(len(timeseries_data)):
                end_ix = i + n_features
                if end_ix > len(timeseries_data)-1:
                    break
                seq_x, seq_y = timeseries_data[i:end_ix], timeseries_data[end_ix]
                X.append(seq_x)
                y.append(seq_y)
            return np.array(X), np.array(y)
        timeseries_data = df["Close"].to_list()
        n_steps = 20
        X, y = prepare_data(timeseries_data, n_steps)
        n_features = 1
        X = X.reshape((X.shape[0], X.shape[1], n_features))
        X.shape
        model = Sequential()
        model.add(LSTM(50, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
        model.add(LSTM(50, activation='relu'))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        model.fit(X, y, epochs=10, verbose=1)
        timeseries_data_last = df["Close"].tail(20).to_list()
        x_input = np.array(timeseries_data_last)
        temp_input=list(x_input)
        lst_output=[]
        i=0
        file_path_and_name = "models/model_day1/"+sec_code+"_"+sec_data.Security_Id+".h5"
        model.save_weights(file_path_and_name)
        while(i<20):
            if(len(temp_input)>20):
                x_input=np.array(temp_input[1:])
                print("{} day input {}".format(i,x_input))
                #print(x_input)
                x_input = x_input.reshape((1, n_steps, n_features))
                #print(x_input)
                yhat = model.predict(x_input, verbose=0)
                print("{} day output {}".format(i,yhat))
                temp_input.append(yhat[0][0])
                temp_input=temp_input[1:]
                #print(temp_input)
                lst_output.append(yhat[0][0])
                i=i+1
            else:
                x_input = x_input.reshape((1, n_steps, n_features))
                yhat = model.predict(x_input, verbose=0)
                print(yhat[0])
                temp_input.append(yhat[0][0])
                lst_output.append(yhat[0][0])
                i=i+1
        print(lst_output)
        forecast_data = Security_Forecast.objects.create(
            Security_Code = sec_data.Security_Code,
            Security_Name = sec_data.Security_Name,
            forecasted_day1 =  lst_output[0],
            forecasted_day2 =  lst_output[1],
            forecasted_day3 =  lst_output[2],
            forecasted_day4 =  lst_output[3],
            forecasted_day5 =  lst_output[4],
            forecasted_day6 =  lst_output[5],
            forecasted_day7 =  lst_output[6],
            forecasted_day8 =  lst_output[7],
            forecasted_day9 =  lst_output[8],
            forecasted_day10 =  lst_output[9],
            forecasted_day11 =  lst_output[10],
            forecasted_day12 =  lst_output[11],
            forecasted_day13 =  lst_output[12],
            forecasted_day14 =  lst_output[13],
            forecasted_day15 =  lst_output[14],
            forecasted_day16 =  lst_output[15],
            forecasted_day17 =  lst_output[16],
            forecasted_day18 =  lst_output[17],
            forecasted_day19 =  lst_output[18],
            forecasted_day20 =  lst_output[19],
        )
        forecast_data.save()
# sec()




class Security_forecast_API(APIView):
    def get(self,request):
        Company_name = request.GET["name"]
        forecast_data = Security_Forecast.objects.filter(Security_Code=Company_name)
        for data in forecast_data:
            Security_Name    = data.Security_Name   
            Predicted_day    = data.Predicted_day   
            forecasted_day1  = float(data.forecasted_day1)
            forecasted_day2  = float(data.forecasted_day2)
            forecasted_day3  = float(data.forecasted_day3)
            forecasted_day4  = float(data.forecasted_day4)
            forecasted_day5  = float(data.forecasted_day5)
            forecasted_day6  = float(data.forecasted_day6)
            forecasted_day7  = float(data.forecasted_day7)
            forecasted_day8  = float(data.forecasted_day8) 
            forecasted_day9  = float(data.forecasted_day9) 
            forecasted_day10 = float(data.forecasted_day10)
            forecasted_day11 = float(data.forecasted_day11)
            forecasted_day12 = float(data.forecasted_day12)
            forecasted_day13 = float(data.forecasted_day13)
            forecasted_day14 = float(data.forecasted_day14)
            forecasted_day15 = float(data.forecasted_day15)
            forecasted_day16 = float(data.forecasted_day16)
            forecasted_day17 = float(data.forecasted_day17)
            forecasted_day18 = float(data.forecasted_day18)
            forecasted_day19 = float(data.forecasted_day19)
            forecasted_day20 = float(data.forecasted_day20)
        
        res = [
            ['Day','Price'],
            [1,forecasted_day1],
            [2,forecasted_day2],
            [3,forecasted_day3],
            [4,forecasted_day4],
            [5,forecasted_day5],
            [6,forecasted_day6],
            [7,forecasted_day7],
            [8,forecasted_day8],
            [9,forecasted_day9],
            [10,forecasted_day10],
            [11,forecasted_day11],
            [12,forecasted_day12],
            [13,forecasted_day13],
            [14,forecasted_day14],
            [15,forecasted_day15],
            [16,forecasted_day16],
            [17,forecasted_day17],
            [18,forecasted_day18],
            [19,forecasted_day19],
            [20,forecasted_day20],
            ]
        return Response(res)




class top_gainers(APIView):
    def get(self,request):
        top_gainers = nse.get_top_gainers()
        return Response(top_gainers)

# class top_losers(APIView):
#     def get(self,request):
#         top_losers = nse.get_top_losers()
#         return Response(top_losers)


# def sec():
#     data  = Security_Name.objects.all()
#     for i in data:
#         sec_code = data.Security_Id

# def company():
#     all_stock_codes = nse.get_stock_codes()
#     print(all_stock_codes)



# # company()


# def sec():
#     data  = Security_Name.objects.all()
#     for i in data:
#         print(i.Security_Code , "-",i.Security_Name)
# sec()

# def sec():
#     data  = Security_Name.objects.all()
#     Security_Code_list = []
#     Security_Id_list = []
#     Security_Name_list = []
#     for i in data:
#         Security_Code_list.append(i.Security_Code) 
#         Security_Id_list.append(i.Security_Id)
#         Security_Name_list.append(i.Security_Name)
#     df_data = {"Security_Code":Security_Code_list,"Security_Id":Security_Id_list,"Security_Name":Security_Name_list,}
#     df = pd.DataFrame(df_data)
#     df.to_csv("nse_stock_with_bse_code.csv")
# # sec()