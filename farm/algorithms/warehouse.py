import numpy as np
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
import joblib
from keras.layers import LSTM, Dropout, Dense
from keras import Sequential
from math import sqrt
from matplotlib import pyplot
import tensorflow as tf
import keras.backend as K
import plotly.express as px
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def forecast():
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
    px.line(df)
    graphic = plot(px, output_type='div')

    return graphic
    

