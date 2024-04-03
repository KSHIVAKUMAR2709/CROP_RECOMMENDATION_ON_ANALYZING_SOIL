import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
# load dataset
data = pd.read_excel("C:\\Users\\prakash\\Downloads\\crop.xlsx")
data= data.drop(data.loc[data['CROP'] == 'jute'].index)
data= data.drop(data.loc[data['CROP'] == 'coffee'].index)
data= data.drop(data.loc[data['CROP'] == 'papaya'].index)
data= data.drop(data.loc[data['CROP'] == 'muskmelon'].index)
data= data.drop(data.loc[data['CROP'] == 'pomegranate'].index)
data= data.drop(data.loc[data['CROP'] == 'mungbean'].index)
data= data.drop(data.loc[data['CROP'] == 'mothbeans'].index)
data= data.drop(data.loc[data['CROP'] == 'pigeonpeas'].index)
data= data.drop(data.loc[data['CROP'] == 'kidneybeans'].index)
data= data.drop(data.loc[data['CROP'] == 'chickpea'].index)
data= data.drop(data.loc[data['CROP'] == 'orange'].index)
data= data.drop(data.loc[data['CROP'] == 'lentil'].index)

def crop_names(x):
    if x=='rice':
        return 1
    if x=='cotton':
        return 2
    if x=='maize':
        return 3
    if x=='mango':
        return 4
    if x=='apple':
        return 5
    if x=='watermelon':
        return 6
    if x=='blackgram':
        return 7
    if x=='banana':
        return 8
    if x=='grapes':
        return 9
    if x=='coconut':
        return 10
data["CROP"]=data["CROP"].apply(crop_names)
data['CROP'].unique()
x=data.drop(['CROP'],axis=1).values
y=data.iloc[:,-1].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
model=LogisticRegression(solver='lbfgs', max_iter=60000)
model2=model.fit(x_train,y_train)
import pickle
pickle.dump(model2,open('croprecomd.pkl','wb'))
#import the lib to load / Save the model
'''import joblib  

# Save the model
joblib.dump(model2, "croprecomd.pkl")'''