from django.db import models
import datetime



class Security_Name(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Id = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Name + " - " +  self.Security_Code 



class Security_Name1(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Id = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    def __str__(self):
        return self.Security_Name + " - " +  self.Security_Code 


class Security_Forecast(models.Model):
    Security_Code = models.CharField(max_length=255,default="",)
    Security_Name = models.CharField(max_length=255,default="",)
    Predicted_day =  models.CharField(max_length=255,default=datetime.date.today())
    forecasted_day1 =  models.CharField(max_length=255,default="",)
    forecasted_day2 =  models.CharField(max_length=255,default="",)
    forecasted_day3 =  models.CharField(max_length=255,default="",)
    forecasted_day4 =  models.CharField(max_length=255,default="",)
    forecasted_day5 =  models.CharField(max_length=255,default="",)
    forecasted_day6 =  models.CharField(max_length=255,default="",)
    forecasted_day7 =  models.CharField(max_length=255,default="",)
    forecasted_day8 =  models.CharField(max_length=255,default="",)
    forecasted_day9 =  models.CharField(max_length=255,default="",)
    forecasted_day10 =  models.CharField(max_length=255,default="",)
    forecasted_day11 =  models.CharField(max_length=255,default="",)
    forecasted_day12 =  models.CharField(max_length=255,default="",)
    forecasted_day13 =  models.CharField(max_length=255,default="",)
    forecasted_day14 =  models.CharField(max_length=255,default="",)
    forecasted_day15 =  models.CharField(max_length=255,default="",)
    forecasted_day16 =  models.CharField(max_length=255,default="",)
    forecasted_day17 =  models.CharField(max_length=255,default="",)
    forecasted_day18 =  models.CharField(max_length=255,default="",)
    forecasted_day19 =  models.CharField(max_length=255,default="",)
    forecasted_day20 =  models.CharField(max_length=255,default="",)
    def __str__(self):
        return str(self.Predicted_day) + " - " + self.Security_Code + " - " +  self.Security_Name 



