import joblib
import streamlit as st
import numpy as np

# Loding the model
stock_model = joblib.load("stock_model.pkl")

# Month mapping dictionary
month_map = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

st.title("Yes Bank Stock Closing Price Predictor")

month = st.selectbox("Select Month", list(month_map.keys()))

# Open stock price
open_min_val = 10.0
open_max_val = 277.0

open_price = st.number_input("Open Price (10 - 277)")

if (open_price < open_min_val or open_price > open_max_val):
    st.warning("Open Price outside training range")

# High stock price
high_min_val = 11.0
high_max_val = 286.0

high_price = st.number_input("High Price (11 - 286)")

if (high_price < high_min_val or high_price > high_max_val):
    st.warning("High Price outside training range")


# Low stock price
low_min_val = 10.0
low_max_val = 277.0

low_price = st.number_input("Low Price (10 - 277)")

if (low_price < low_min_val or low_price > low_max_val):
    st.warning("Low Price outside training range")

# Function to pre-process the user input
def preprocessor(month, open_price, high_price, low_price):
    month_num = month_map[month]

    month_sin = np.sin((2 * np.pi * month_num) / 12)
    month_cos = np.cos((2 * np.pi * month_num) / 12)

    open_log = np.log1p(open_price)
    high_log = np.log1p(high_price)
    low_log = np.log1p(low_price)

    features = [[month_sin, month_cos, open_log, high_log, low_log]]
    return features

if st.button("Predict"):
    features = preprocessor(month, open_price, high_price, low_price)
    
    close_log = stock_model.predict(features)[0]

    close_price = np.expm1(close_log)

    st.success(f"Predicted Close Price = {close_price:.2f}")