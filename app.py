# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ZF3By0fZARb6thJ0yqzl5OUhJJRDyFU
"""

pip install Flask

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based model for demonstration purposes
def predict_click(age, gender, income):
    if age < 30 and gender == 'male' and income > 50000:
        return "80% Click Probability"
    else:
        return "30% Click Probability"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    gender = request.form['gender']
    income = int(request.form['income'])

    prediction = predict_click(age, gender, income)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)