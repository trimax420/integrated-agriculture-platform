import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

df=pd.read_csv('/home/trimax/Desktop/integrated-agriculture-platform/farm/datasets/TemperatureMum 1999-2019.csv')
df_date=[]
for i in range(0,len(df['Month'])):
    date=datetime.date(year=df['Year'][i],month=df['Month'][i],day=df['Day'][i])
    df_date.append(date)

df['Date']=pd.to_datetime(df_date)
df=df.drop(['Month','Day','Year','TempF'],axis=1)

df.set_index("Date", inplace = True)

rolmean=df.rolling(window=52).mean()
rolstd=df.rolling(window=52).std()
