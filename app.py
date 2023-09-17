from flask import Flask, render_template, request
import numpy as np


import pickle
model = pickle.load(open('house.pkl','rb'))

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/predict")
def predicts():
    return render_template("predict.html")

@app.route('/submit', methods =['GET', 'POST']) 
def predict():
    area =float(request.form['area'])
    bedrooms =float(request.form['bedrooms'])
    bathrooms =float(request.form['bathrooms'])
    stories =float(request.form['stories'])
    mainroad =float(request.form['mainroad'])
    guestroom =float(request.form['guestroom'])
    basement =float(request.form['basement'])
    hotwaterheating =float(request.form['hotwaterheating'])
    airconditioning =float(request.form['airconditioning'])
    parking =float(request.form['parking'])
    furnishingstatus =float(request.form['furnishingstatus'])
    
    total = np.array([[ area, bedrooms, bathrooms, stories, mainroad, guestroom, basement, hotwaterheating, airconditioning, parking, furnishingstatus]] )
    prediction = model.predict(total)
    return render_template('submit.html', predict=int(prediction))
    
if __name__ == "__main__":
    app.run(debug=True)