# Yes Bank Stock Closing Price Prediction

## Project Overview

This project aims to predict the monthly closing stock price of Yes Bank using historical stock market data and Machine Learning techniques. The dataset contains datewise stock prices since the bank's inception, including Opening, High, Low, and Closing prices.

Yes Bank became a major topic of discussion in the Indian financial sector due to the fraud case involving its founder, Rana Kapoor. This project explores the relationship between historical stock price variables and evaluates whether machine learning models can accurately predict the bank's closing stock price.

---

## Business Problem

Yes Bank experienced significant fluctuations in its stock prices following major financial and governance-related events. Investors and analysts often rely on historical market data to understand stock behavior and make informed decisions.

The objective of this project is to develop a regression model capable of predicting the monthly closing stock price based on historical stock price information.

---

## Dataset Information

The dataset contains monthly stock price records with the following features:

| Feature | Description                           |
| ------- | ------------------------------------- |
| Date    | Date of observation                  |
| Open    | Opening stock price                   |
| High    | Highest stock price during the month  |
| Low     | Lowest stock price during the month   |
| Close   | Closing stock price (Target Variable) |

Additional cyclical features were created:

* Month_Sin
* Month_Cos

These features help represent the cyclical nature of months.

---

## Project Workflow

### 1. Data Loading

* Imported dataset using Pandas.
* Examined dataset structure and data types.

### 2. Data Cleaning

* Checked for missing values.
* Removed duplicates (if any).
* Verified data consistency.

### 3. Data Manipulation

* Converted month information into cyclical features:

  * Month_Sin
  * Month_Cos

### 4. Exploratory Data Analysis (EDA)

Performed:

* Histograms
* Boxplots
* Line plots
* Correlation heatmap
* Pair plots
* Distribution analysis
* Outlier analysis

### 5. Feature Engineering

* Cyclical encoding of month variable.
* Log transformation of skewed variables (if applicable).

### 6. Model Building

Regression models were trained and evaluated.

Algorithms used:

* Linear Regression
* Random Forest Regressor

---

## Model Evaluation Metrics

The following evaluation metrics were used:

### R² Score

Measures the proportion of variance explained by the model.

### Mean Absolute Error (MAE)

Average absolute prediction error.

### Mean Squared Error (MSE)

Average squared prediction error.

---

## Final Model Performance

| Metric   | Value  |
| -------- | ------ |
| R² Score | 0.9934 |
| MSE      | 0.0033 |
| MAE      | 0.045  |

### Interpretation

* The model explains approximately 99.34% of the variance in closing stock prices.
* Very low prediction error was achieved.
* The model successfully captured the relationship between stock price variables.

---

## Model Explainability (SHAP)

SHAP (SHapley Additive Explanations) was used to understand feature importance.

### Feature Importance Ranking

| Feature   | SHAP Importance |
| --------- | --------------- |
| High      | +0.46           |
| Low       | +0.37           |
| Open      | +0.26           |
| Month_Sin | +0.01           |
| Month_Cos | +0.00           |

### Key Findings

* High price is the most influential feature.
* Low and Open prices also strongly affect predictions.
* Seasonal month-based features contribute very little.
* Stock price information is the primary driver of the model's predictions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* SHAP
* Jupyter Notebook / Google Colab

---

## Project Structure

```text
YesBankStockPricePrediction/
│
├── data/
│   └── yes_bank_stock_data.csv
│
├── notebooks/
│   └── Yes_Bank_Stock_Prediction.ipynb
│
├── images/
│   └── plots/
│
├── README.md
│
└── requirements.txt
```

---

## Results

The developed machine learning model achieved excellent predictive performance with an R² score of 0.9934. SHAP analysis showed that High, Low, and Open prices were the most influential factors in predicting the monthly closing stock price. The project demonstrates the effectiveness of machine learning techniques in analyzing historical stock market data and generating accurate predictions.

---

## Author

Name: Chaitanya Jaunjal

Project: Yes Bank Stock Closing Price Prediction

Domain: Machine Learning / Financial Analytics
