from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np


app = Flask(__name__)

with open(r'flask app/model.pkl', 'rb') as f:
    model = pickle.load(f)

df = pd.read_csv('datasets/laptops_cleaned.csv', dtype={'processor_tier': str, 'ram': str, 'storage': str, 'vram': str})

@app.route('/')
def home():
    options = {
        'Brand': sorted(df['Brand'].unique().tolist()),
        'processor_brand': sorted(df['processor_brand'].unique().tolist()),
        'ram': sorted(df['ram'].unique().tolist()),
        'storage': sorted(df['storage'].unique().tolist()),
        'screen_size': sorted(df['screen_size'].unique().tolist()),
        'display_type': sorted(df['display_type'].unique().tolist()),
        'gpu_brand': sorted(df['gpu_brand'].unique().tolist())

    }
    
    # mapping for dependent dropdowns
    proc_series_map = df.groupby('processor_brand')['processor_series'].unique().apply(list).to_dict()
    proc_tier_map = df.groupby('processor_brand')['processor_tier'].unique().apply(list).to_dict()
    gpu_model_map = df.groupby('gpu_brand')['gpu_model'].unique().apply(list).to_dict()
    vram_map = df.groupby('gpu_brand')['vram'].unique().apply(list).to_dict()

    return render_template('index.html', options=options, 
                          proc_series_map=proc_series_map, 
                          proc_tier_map=proc_tier_map,
                          gpu_model_map=gpu_model_map,
                          vram_map=vram_map)

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

    def format_indian(num):
        s = str(int(num))
        if len(s) <= 3:
            return s
        last3 = s[-3:]
        rest = s[:-3]
        parts = []
        while len(rest) > 2:
            parts.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.append(rest)
        return ','.join(reversed(parts)) + ',' + last3

    return jsonify({
        "predicted_price": format_indian(round(prediction, 2))
    })

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=False)
