from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import loginForm,registrationForm,farmerForm,research_agroForm,drone_operatorForm,kvkForm,warehouseForm,registrationForm,fieldForm,wareForm
from .models import login
from farm.algorithms import crop_rec,crop_hel,warehouse
import numpy as np
from django.http import StreamingHttpResponse
import cv2
import threading
from django.views.decorators import gzip
import plotly.express as px
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import BayesianRidge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import HuberRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae


def home(request):
    return render(request,'index.html')

def login_page(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if login.objects.filter(userid=username ,password=password).exists() == True :
                return redirect(index)
            else:
                return HttpResponse('error')

            
    else:
        return render(request,'login.html')
    

def register(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            adhaar_number = form.cleaned_data['adhaar_number']
            name = form.cleaned_data['name']
            request.session['adhaar_number'] = adhaar_number
            request.session['role'] = role
            request.session['name'] = name
            l = login(userid = name,password = adhaar_number,role = role)
            l.save()
            form.save()
            return redirect(role_registrations)
           
    else:
        form = registrationForm()
    return render(request,'register.html',{'form':form})

def role_registrations(request):
    role = request.session['role']
    adhaar_number = request.session['adhaar_number']
    if role == 'Farmer':
               if request.method == 'POST':
                   form_role = farmerForm(request.POST)
                   form_role.save()
                   return HttpResponse('sucessful')
               else:
                   form_role = farmerForm()
               return render(request,'register.html',{'form':form_role})
           
    elif role == 'Researcher' or role == 'Agro-scientist':
        if request.method == 'POST':
            form_role = research_agroForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = research_agroForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'Drone Operator' :
        if request.method == 'POST':
            form_role = drone_operatorForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = drone_operatorForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'KVK':
        if request.method == 'POST':
            form_role = kvkForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = kvkForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'Warehouse' or role == 'Food Processor' or role == 'Distributer' or role == 'Retailer':
        if request.method == 'POST':
            form_role = warehouseForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = warehouseForm()
        return render(request,'register.html',{'form':form_role})
           
    elif role == 'Others':
        if request.method == 'POST':
            form_role = farmerForm(request.POST)
            form_role.save()
            return HttpResponse('sucessful')
        else:
            form_role = farmerForm()
        return render(request,'register.html',{'form':form_role})

def index(request):
    return render(request,'page2.html')

def croprec(request):
    ranfor = crop_rec.RDF()
    xgb = crop_rec.XGB()
    le = crop_rec.label_encoder
    if request.method == 'POST':
        form = fieldForm(request.POST)
        if form.is_valid():
            temp = form.cleaned_data['temp']
            humi = form.cleaned_data['humi']
            ph = form.cleaned_data['ph']
            rain = form.cleaned_data['rain']
            val = ranfor.predict(np.array([temp,humi,ph,rain]).reshape(1,-1))
            val = le.inverse_transform(val)
        return render(request,"croprec.html",{'form':form,'val':val})
    
    else:
        form = fieldForm()
        return render(request,"croprec.html",{'form':form})

def weather(request):
    
    return render(request,'weather.html')

def warehouse(request):
    '''
    form = wareForm()
    if request.method == 'POST':
        form = wareForm(request.POST,request.FILES)
        if 'file' in request.FILES:
            if form.is_valid():
                file = handle_uploaded_file(request.FILES['file'])
                file = pd.read_csv(file)
                graphic = warehouse.fore(file)
                return render(request,"warehouse.html",{"warehouse":graphic})

    else:
    '''
    df = pd.read_csv('/home/trimax/Desktop/integrated-agriculture-platform/farm/datasets/warehouse/61_1445.csv')
    df.drop(columns=['meal_id','center_id'], inplace=True)
    df.set_index(['week'],inplace=True)
    df[['checkout_price', 'base_price', 'diff']]/=100

    X= df.drop(columns=['num_orders']).values
    Y= df.num_orders.values
    X.reshape(-1,5)
    Y.reshape(-1)

    pipe3= Pipeline([('poly', PolynomialFeatures(degree=1, include_bias=True)),
                    ('KNN', KNeighborsRegressor(n_neighbors=100, weights='distance' ))])

    X_train, X_val, y_train, y_val= train_test_split( X, Y, test_size=0.15, random_state=101)

    t=pipe3.fit(X_train, y_train)
    pred3= pipe3.predict(X_val)
    #print(mae(y_train, pipe3.predict(X_train)))
    #mae(y_val, pred3)
    data = {'real':Y,'Predicted':pipe3.predict(X)}
    df = pd.DataFrame(data)
    plot_1=px.line(df)
    graphic = plot(plot_1, output_type='div')
    
    return render(request,"warehouse.html",{"warehouse":graphic})
    

def crophel(request):
    crop_hel.main()
    return redirect(index)