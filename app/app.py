import os
from flask import Flask, render_template, request
from Models.model import Modelr
import pandas as pd
import numpy as np

app = Flask(__name__)

# initialize the model
model = Modelr('app/trained_model/model.pkl')

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get feature values from form input
    ph = float(request.form['ph'])
    hardness = float(request.form['hardness'])
    solids = float(request.form['solids'])
    chloramines = float(request.form['chloramines'])
    sulfate = float(request.form['sulfate'])
    conductivity = float(request.form['conductivity'])
    organic_carbon = float(request.form['organic_carbon'])
    trihalomethanes = float(request.form['trihalomethanes'])
    turbidity = float(request.form['turbidity'])
    
    # predire
    features = np.array([[ ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction_list = model.predict(features)
    prediction_str = str(prediction_list).replace("]", "").replace("[", "").strip()
    prediction = round(float(prediction_str),2)
    if prediction ==1:
        prediction = "drinkable"
    else:
        prediction = "not drinkable"
    
    return render_template('result.html', prediction=prediction)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)