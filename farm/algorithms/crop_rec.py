import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from xgboost import XGBClassifier

data=pd.read_csv('farm/datasets/Crop_recommendation.csv')
data=data.drop(['N','P','K'],axis=1)

label_encoder = LabelEncoder()
X = data.drop(['label'],axis=1)
y = label_encoder.fit_transform(data["label"])

X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size = 0.15, random_state = 0)


def RDF():

    pipeline = make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=9,random_state=128))
    pipeline.fit(X_train, y_train)

    # Test Data Metrics
    #predictions = pipeline.predict(X_test)
    #accuracy = accuracy_score(y_test, predictions)
    #print(f"Accuracy on Test Data: {accuracy*100}%")

    # Whole Data Metrics
    #predictions = pipeline.predict(X.values)
    #accuracy = accuracy_score(y, predictions)
    #print(f"Accuracy on Whole Data: {accuracy*100}%")

    return pipeline

def XGB():
    knn_pipeline = make_pipeline(StandardScaler(), XGBClassifier(random_state=128))
    knn_pipeline.fit(X_train, y_train)

    # Test Data Metrics
    #predictions = knn_pipeline.predict(X_test)
    #accuracy = accuracy_score(y_test, predictions)
    #print(f"Accuracy on Test Data: {accuracy*100}%")

    # Whole Data Metrics
    #predictions = knn_pipeline.predict(X.values)
    #accuracy = accuracy_score(y, predictions)
    #print(f"Accuracy on Whole Data: {accuracy*100}%")

    return knn_pipeline
