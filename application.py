from flask import Flask,request,render_template,jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler




application=Flask(__name__)
app=application

ridge_model=pickle.load(open('ridge.pkl','rb'))
standard_scaler=pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
      Temperature=float(request.form.get('temprature'))
      RH=float(request.form.get('RH'))
      Ws=float(request.form.get('ws'))
      Rain=float(request.form.get('rain'))
      FFMC=float(request.form.get('FFMC'))
      DMC=float(request.form.get('DMC'))
      ISI=float(request.form.get('ISI'))
      Classes=float(request.form.get('classes'))
      Region=float(request.form.get('region'))

      new_standard_data=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
      result=ridge_model.predict(new_standard_data)
      
   
      return render_template('home.html',results_score=result[0])
    
    else:
        return render_template('home.html',results_score='please enter the data first')
if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
