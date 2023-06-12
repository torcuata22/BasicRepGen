from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
from pandas.io import json
from .models import Data

# Create your views here.
def hello(request):
    if request.method == 'POST':
        #get all the data:
        Data.objects.all()
        myfile=request.FILES['file']
        df=pd.read_csv(myfile)
        json_records=df.reset_index().to_json(orient='records')
        data=[]
        #create list of properties
        data = json.loads(json_records)
        for d in data:
            name = d['property_name']
            price = d['property_price']
            rent = d['property_rent']
            emi = d['emi']
            tax = d['tax']
            exp = d['other_exp']
            dt = Data(name=name, price=price, rent=rent, emi=emi, tax=tax, exp=exp) #created data object, now save to database:
            dt.save()


    print("this is a GET request")
    return render(request, 'myapp/index.html')