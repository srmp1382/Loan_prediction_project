import numpy as np
import flask
import pickle as pkl
from flask import Flask, request, jsonify
import sklearn
from sklearn.preprocessing import StandardScaler, MinMaxScaler

app=Flask(__name__)

@app.route('/')
def home():
    return "This is my nice home page\n I am still learning it"

@app.route('/display', methods=['POST'])
def display():
    with open('my_classifier.pkl', 'rb') as file_name:
        clf=pkl.load(file_name)
    data=request.get_json()
    if data['Gender']=='Male':
        gender=1
    else:
        gender=0
    if data['Education']=='Graduate':
        education=1
    else:
        education=0
    if data['Married']=='Yes':
        married=1
    else:
        married=0
    if data['Self_Employed']=='Yes':
        self_employed=1
    else:
        self_employed=0
    if data['Property_Area']=='Rural':
        property_area=0
    elif data['Property_Area']=='Semiurban':
        property_area=1
    else:
        property_area=2
    dep=int(data['Dependents'])
    app_inc=float(data['ApplicantIncome'])
    coapp_inc=float(data['CoapplicantIncome'])
    loan_amt=float(data['Loan_Amount'])
    loan_term=float(data['Loan_Amount_Term'])
    cred_hist=float(data['Credit_History'])
    result=clf.predict(np.array([[gender, married,dep, education, self_employed, app_inc, coapp_inc, loan_amt, loan_term, cred_hist, property_area]]).reshape(1,-1))
    if result==1:
        return "rejected"
    else:
        return "approved"

