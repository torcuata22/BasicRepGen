from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd 
from pandas.io import json

# Create your views here.
def hello(request):
    if request.method == 'POST':
        myfile=request.FILES['file']
        df=pd.read_csv(myfile)
        json_records=df.reset_index().to_json(orient='records')
        data=[]
        #create list of properties
        data = json.loads(json_records)
        print(data)
       
    print("this is a GET request")
    return render(request, 'myapp/index.html')