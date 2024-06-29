from rest_framework import serializers 
from backendapp import models
  
# class ReactSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = models.One 
#         fields = '__all__'

class List_company_ser(serializers.ModelSerializer):
    class Meta:
        model= models.Company_list
        fields='__all__'

class List_company_Bse_nse_code(serializers.ModelSerializer):
    class Meta:
        model= models.Security_Name_nse_bse_code
        fields='__all__'

class Security_user_analyse_tool_data_ser(serializers.ModelSerializer):
    class Meta:
        model= models.Security_user_analyse_tool_data
        fields='__all__'

class List_company_ser_sec(serializers.ModelSerializer):
    class Meta:
        model= models.Company_list
        fields=['Security_Code']

class Top_ratios_ser(serializers.ModelSerializer):
    class Meta:
        model= models.Top_ratios
        fields='__all__'


class Security_Name_ser(serializers.ModelSerializer):
    class Meta:
        model= models.Security_Name
        fields='__all__'

class Security_News_ser(serializers.ModelSerializer):
    class Meta:
        model= models.Security_News
        fields='__all__'