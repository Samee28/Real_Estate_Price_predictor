from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('home_price_model.pkl', 'rb'))  # Make sure model.pkl is in same folder

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(f)) for f in [
            'crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age',
            'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat'
        ]]
        prediction = model.predict([features])[0]
        predicted_price = round(prediction, 2)
        return render_template(
            'index.html',
            prediction_text=f"Estimated Home Price: ${predicted_price}k",
            predicted_price=predicted_price
        )
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
