# Laptop Price Predictor 

A machine learning web app that predicts laptop prices based on specifications like brand, processor, RAM, storage, display, and GPU. Built end-to-end from data scraping to deployment.

**Live Demo**: [laptop-price-predictor-ru5l.onrender.com](https://laptop-price-predictor-ru5l.onrender.com)

> Note: The app is hosted on Render's free tier and may take 50+ seconds to load on first visit due to inactivity spin-down.

---

## Project Overview

This project covers the complete data science pipeline:

1. **Data Collection** — Scraped laptop listings from Vijay Sales using Selenium and BeautifulSoup
2. **Data Cleaning** — Extracted structured features from messy raw strings (processor names, GPU specs, display types)
3. **Exploratory Data Analysis** — Analyzed price distributions, brand comparisons, and feature correlations using Matplotlib, Seaborn, and Plotly
4. **Feature Engineering** — Split processor strings into brand/series/tier, extracted GPU brand/model/VRAM, normalized display types
5. **Model Building** — Built a preprocessing pipeline with Ordinal Encoding, One-Hot Encoding, and Standard Scaling, trained with Linear Regression
6. **Deployment** — Flask web app with interactive dropdowns deployed on Render

---

## Results

| Model | Cross-Val R² | Test R² |
|---|---|---|
| Linear Regression | 0.87 | 0.84 |
| Random Forest | 0.85 | 0.74 |

Linear Regression outperformed Random Forest on this dataset, likely due to the high proportion of categorical features and the relatively small dataset size (~314 rows).

---

## Features

- **Predict Page** — Select laptop specs from dependent dropdowns (processor series filters based on brand, GPU model filters based on GPU brand) and get an estimated price
- **Analysis Page** — Interactive Plotly charts showing brand distribution, price distribution, GPU share, and price vs RAM
- **About Page** — Project summary and links

---

## Tech Stack

- **Data Collection**: Selenium, BeautifulSoup
- **Data Processing**: Pandas, NumPy
- **EDA**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: scikit-learn (Pipeline, OrdinalEncoder, OneHotEncoder, StandardScaler, LinearRegression)
- **Web App**: Flask
- **Deployment**: Render

---

## Dataset

Raw and cleaned datasets are available on Kaggle:
[Vijay Sales Laptop Dataset (Raw + Cleaned)](https://www.kaggle.com/datasets/himanshusingh4441/cleaned-laptop-dataset)

Data scraped from [Vijay Sales](https://www.vijaysales.com) for educational purposes.

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/himanshu0154/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor

# Install dependencies
pip install -r flask_app/requirements.txt

# Run the app
cd flask_app
python app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

---

## Project Structure

```
Laptop-Price-Predictor/
├── flask_app/
│   ├── app.py
│   ├── model.pkl
│   ├── laptops_cleaned.csv
│   ├── requirements.txt
│   ├── Procfile
│   ├── static/
│   │   ├── style.css
│   │   └── plots/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── analysis.html
│       └── about.html
├── data cleaning.ipynb
├── EDA.ipynb
├── model.ipynb
└── Scraper/
```

---

Made by [Himanshu](https://github.com/himanshu0154)
