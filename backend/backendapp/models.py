from django.db import models 
  
# Create your models here. 
  
class Company_list(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Issuer_Name = models.CharField(max_length=255,default="",)
    Security_Id = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Status = models.CharField(max_length=255,default="",)
    Group = models.CharField(max_length=255,default="",)
    Face_Value = models.CharField(max_length=255,default="",)
    ISIN_No = models.CharField(max_length=255,default="",)
    Industry = models.CharField(max_length=255,default="",)
    Instrument = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Id + " - " +  self.Security_Name 

class Top_ratios(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Security_Id = models.CharField(max_length=255,default="",)
    Market_Cap = models.CharField(max_length=255,default="",)
    Current_Price = models.CharField(max_length=255,default="",)
    High= models.CharField(max_length=255,default="",)
    Low = models.CharField(max_length=255,default="",)
    Stock_PE = models.CharField(max_length=255,default="",)
    Book_Value = models.CharField(max_length=255,default="",)
    Dividend_Yield = models.CharField(max_length=255,default="",)
    ROCE = models.CharField(max_length=255,default="",)
    ROE = models.CharField(max_length=255,default="",)
    Face_Value = models.CharField(max_length=255,default="",)
    About = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Name + " - " +  self.Security_Code 

class Security_Index(models.Model):
    Security_exchange = models.CharField(max_length=255,default="",)
    Security_index_name = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_exchange + " - " +  self.Security_index_name 

class Security_Name(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Id = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Name + " - " +  self.Security_Code 

class Security_Name_nse_bse_code(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Id = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Name + " - " +  self.Security_Code 

class Security_News(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Security_News = models.TextField()
    Sentiment_Pos = models.CharField(max_length=255,default="",)
    Sentiment_Neg = models.CharField(max_length=255,default="",)
    Sentiment_Neu = models.CharField(max_length=255,default="",)
    Sentiment_Com = models.CharField(max_length=255,default="",)
    Sentiment_Overall = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Name + " - " +  self.Security_News 


class Security_Balance(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Share_Capital = models.CharField(max_length=255,default="",)
    Reserves      = models.CharField(max_length=255,default="",)
    Borrowings    = models.CharField(max_length=255,default="",)
    Other_Liabilities = models.CharField(max_length=255,default="",)
    Total_Liabilities = models.CharField(max_length=255,default="",)
    Fixed_Assets = models.CharField(max_length=255,default="",)
    CWIP         = models.CharField(max_length=255,default="",)
    Investments  = models.CharField(max_length=255,default="",)
    Other_Assets = models.CharField(max_length=255,default="",)
    Total_Assets = models.CharField(max_length=255,default="",)   
    def __str__(self):
        return self.Security_Code + " - " +  self.Security_Name


class Security_ShareHolding(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Promoters_dec_2020 = models.CharField(max_length=255,default="",)
    Promoters_sep_2020 = models.CharField(max_length=255,default="",)
    FIIs_dec_2020 = models.CharField(max_length=255,default="",)
    FIIs_sep_2020 = models.CharField(max_length=255,default="",)
    Mutual_Funds_dec_2020 = models.CharField(max_length=255,default="",)
    Mutual_Funds_sep_2020 = models.CharField(max_length=255,default="",)
    Insurance_Companies_dec_2020 = models.CharField(max_length=255,default="",)
    Insurance_Companies_sep_2020 = models.CharField(max_length=255,default="",)
    Other_DIIs_dec_2020 = models.CharField(max_length=255,default="",)
    Other_DIIs_sep_2020 = models.CharField(max_length=255,default="",)
    Non_Institution_dec_2020 = models.CharField(max_length=255,default="",)
    Non_Institution_sep_2020 = models.CharField(max_length=255,default="",)
   
    def __str__(self):
        return self.Security_Code + " - " +  self.Security_Name



class Security_Quarter_Result(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Sales = models.CharField(max_length=255,default="",)
    Expenses = models.CharField(max_length=255,default="",)
    Operating_profit = models.CharField(max_length=255,default="",)
    Opm = models.CharField(max_length=255,default="",)
    Other_income = models.CharField(max_length=255,default="",)
    Interest = models.CharField(max_length=255,default="",)
    Depreciation = models.CharField(max_length=255,default="",)
    Profit_before_tax = models.CharField(max_length=255,default="",)
    Tax_percentage = models.CharField(max_length=255,default="",)
    Net_profit = models.CharField(max_length=255,default="",)
    Eps = models.CharField(max_length=255,default="",)
    year = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Code + " - " +  self.Security_Name


class Security_Quarter_Result_yoy_data(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Sales = models.CharField(max_length=255,default="",)
    Expenses = models.CharField(max_length=255,default="",)
    Operating_profit = models.CharField(max_length=255,default="",)
    Opm = models.CharField(max_length=255,default="",)
    Other_income = models.CharField(max_length=255,default="",)
    Interest = models.CharField(max_length=255,default="",)
    Depreciation = models.CharField(max_length=255,default="",)
    Profit_before_tax = models.CharField(max_length=255,default="",)
    Tax_percentage = models.CharField(max_length=255,default="",)
    Net_profit = models.CharField(max_length=255,default="",)
    Eps = models.CharField(max_length=255,default="",)
    year = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Code + " - " +  self.Security_Name



class Security_user_analyse_tool_data(models.Model):
    Symbol                 = models.CharField(max_length=255,default="",) 
    Trade_Date			   = models.CharField(max_length=255,default="",) 
    Exchange	           = models.CharField(max_length=255,default="",)
    Segment                = models.CharField(max_length=255,default="",)
    Series	               = models.CharField(max_length=255,default="",)
    Trade_Type	           = models.CharField(max_length=255,default="",)
    Quantity	           = models.CharField(max_length=255,default="",)
    Price	               = models.CharField(max_length=255,default="",)
    Trade_ID	           = models.CharField(max_length=255,default="",)
    Order_ID	           = models.CharField(max_length=255,default="",)
    Order_Execution_Time   = models.CharField(max_length=255,default="",)
    dataset_id             = models.CharField(max_length=255,default="",)
    user_id                = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Symbol + " - " +  self.user_id
