from django.shortcuts import render 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from nsetools import Nse
import yfinance as yf
import json
import pandas as pd
from json import encoder


# Create your views here.

nse = Nse()

class top_gainers(APIView):
    def get(self,request):
        # top_gainers = nse.get_top_gainers()
        top_gainers = {"lastPrice": 19000, "change": 10000, "pChange":12}

        return Response(top_gainers)
class top_losers(APIView):
    def get(self,request):
        # top_losers = nse.get_top_losers()
        top_gainers = {"lastPrice": 19000, "change": 10000, "pChange":12}
        return Response(top_losers)


class nifty(APIView):
    def get(self,request):
        # data = nse.get_index_quote("nifty 50")
        data = {"lastPrice": 19000, "change": 10000, "pChange":12}
        Close  = data["lastPrice"]
        change = data["change"]
        pChange = data["pChange"]
      
        if float(data["change"]) > 0:
            color = "success"
        else:
            color = "danger"
        dict_df = [{"lastPrice":Close,"change":change,"pChange":pChange,"color":color}]
        df_f = pd.DataFrame(dict_df)
        result = df_f.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)
        
class nifty_mid_50(APIView):
    def get(self,request):
        # data = nse.get_index_quote("NIFTY MIDCAP 50")
        data = {"lastPrice": 19000, "change": 10000, "pChange":12}

        Close  = data["lastPrice"]
        change = data["change"]
        pChange = data["pChange"]
      
        if float(data["change"]) > 0:
            color = "success"
        else:
            color = "danger"
        dict_df = [{"lastPrice":Close,"change":change,"pChange":pChange,"color":color}]
        df_f = pd.DataFrame(dict_df)
        result = df_f.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)
        
class nifty_next_50(APIView):
    def get(self,request):
        # data = nse.get_index_quote("NIFTY NEXT 50")
        data = {"lastPrice": 19000, "change": 10000, "pChange":12}

        Close  = data["lastPrice"]
        change = data["change"]
        pChange = data["pChange"]
      
        if float(data["change"]) > 0:
            color = "success"
        else:
            color = "danger"
        dict_df = [{"lastPrice":Close,"change":change,"pChange":pChange,"color":color}]
        df_f = pd.DataFrame(dict_df)
        result = df_f.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)
        
class nifty_auto(APIView):
    def get(self,request):
        # data = nse.get_index_quote("NIFTY 500")
        data = {"lastPrice": 19000, "change": 10000, "pChange":12}

        Close  = data["lastPrice"]
        change = data["change"]
        pChange = data["pChange"]
      
        if float(data["change"]) > 0:
            color = "success"
        else:
            color = "danger"
        dict_df = [{"lastPrice":Close,"change":change,"pChange":pChange,"color":color}]
        df_f = pd.DataFrame(dict_df)
        result = df_f.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)
        
class nifty_bank(APIView):
    def get(self,request):
        
        # data = nse.get_index_quote("nifty bank")
        data = {"lastPrice": 19000, "change": 10000, "pChange":12}

        Close  = data["lastPrice"]
        change = data["change"]
        pChange = data["pChange"]
      
        if float(data["change"]) > 0:
            color = "success"
        else:
            color = "danger"
        dict_df = [{"lastPrice":Close,"change":change,"pChange":pChange,"color":color}]
        df_f = pd.DataFrame(dict_df)
        result = df_f.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)
        
class nifty_small_cap_50(APIView):
    def get(self,request):
        
        # data = nse.get_index_quote("INDIA VIX")
        data = {"lastPrice": 19000, "change": 10000, "pChange":12}

        Close  = data["lastPrice"]
        change = data["change"]
        pChange = data["pChange"]
      
        if float(data["change"]) > 0:
            color = "success"
        else:
            color = "danger"
        dict_df = [{"lastPrice":Close,"change":change,"pChange":pChange,"color":color}]
        df_f = pd.DataFrame(dict_df)
        result = df_f.to_json(orient="records")
        datas = json.loads(result)
        return Response(datas)
