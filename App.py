import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Resale Car Price Prediction")
year = st.sidebar._number_input("Registered Year",step=1, min_value=1985)
encap = st.sidebar._number_input("Engine Capacity", step=1, min_value=1000)
insurance = st.sidebar.selectbox("Insurance", options=["Third Party", "Comprehensive",
                                            "Zero Dep", "Not Available", "First", "Third"])
trans = st.sidebar.selectbox("Transmission Type", options=["Manual", "Automatic"])
kms = st.sidebar._number_input("Kilometers Driven", min_value=0, step=1)
owner = st.sidebar.selectbox("Owner", options=["First Owner", "Second Owner", "Third Owner", 
                                        "Fourth Owner", "Fifth Owner"])
fuel = st.sidebar.selectbox("Fuel Type", options=["Petrol", "Diesel"])
maxPow = st.sidebar._number_input("Max Power (BHP)", min_value=0.0)
seat = st.sidebar._number_input("Seats", min_value=1)
mileage = st.sidebar._number_input("Mileage", min_value=0.0)

if st.sidebar.button("Predict"):
    df = pd.DataFrame({"registered_year":[year], "engine_capacity":[encap],
                       "insurance":[insurance], "transmission_type":[trans],
                       "kms_driven":[kms], "owner_type":[owner],
                       "fuel_type":[fuel], "max_power":[maxPow],
                       "seats": [seat],"mileage":[mileage]})
    price = model.predict(df)
    st.subheader(f"The Resale Price of the car is : {price[0]:.3f} Lakhs")

