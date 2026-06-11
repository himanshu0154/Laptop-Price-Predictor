from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np


app = Flask(__name__)

with open(r'flask app/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    df = pd.DataFrame([data])

    df['processor_tier'] = df['processor_tier'].astype(str)
    df['ram'] = df['ram'].astype(str)
    df['vram'] = df['vram'].astype(str)
    df['screen_size'] = df['screen_size'].astype(float)
        
    print(df.dtypes)

    prediction = model.predict(df)[0]
    prediction = np.expm1(prediction)
    return jsonify({
        "predicted_price": round(prediction, 2)
    })




if __name__ == "__main__":
    app.run(debug=True)
