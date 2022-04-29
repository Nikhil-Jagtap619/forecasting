import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from math import sqrt
from sklearn.metrics import mean_squared_error

st.set_page_config(page_title="Demand forecast")


def main():
    st.title("Demand Forecasting")
    st.write("This is an overview of Beer Manufacturing data forecasting that we had as a project.\nThe goal was to predict order quantity of beers from 2020-05-01 to 2020-05-15 using verious Forecasting Mehtods.\nBelow you can check how close forecasts are to the actual values(Cross Validation).")
    tech = ["SimpleExponentialSmoothing","Holt's Linear Trend","Holt's Winter","ARIMA","SARIMA","FBprophet"]

    data = pd.read_csv("prediction3.csv")
    data.drop("Unnamed: 0", axis=1, inplace=True)
    data.set_index("Date", inplace=True)
    st.dataframe(data)
    st.write("## Techniques Used")
    for t in tech:
        st.write(t)

    #plotting
    ls = data.columns.tolist()
    choice = st.multiselect("Choose Forecasting Methods",ls,default="Actual values")
    user = data[choice]
    fig = plt.figure()
    st.line_chart(user)

    #Evaluation Metric
    st.subheader("Evaluation Metrics")
    score = 0
    agree = st.button("show RMSE score")
    if agree:
        for i in user.columns:
            if i!="Actual values":
                score = sqrt(mean_squared_error(user[i].values, data["Actual values"].values))
                txt = f"Mean Squared Error for {st.write(i)}: {st.success(round(score,2))}"
                # st.write(txt)

    st.subheader("Comparison of values")
    comp = st.button("Show")
    if comp:
        st.table(user)

    st.info("My Review")
    txt2 = "🔹 As you can see Simple Exponential Smoothing, Holt's linear & ARIMA shows really awful predictions \n however, SARIMA, Holt's Winter & FBprophet shows some decent Forecasting"
    txt3 = "🔹 The Series has Noise, which means there are values which are higher than expectations\n probably due to Events, one of the reasons that beer quanity gone skyrocket"
    txt4 = "🔹 Even though the data was stationary, i had to stationarise a bit more to get more accuracy"
    txt5 = "🔹 Demand forecasting can be improved with DEEP LEARNIGN techniques\nI'll use those in the upcoming period of time"
    for j in [txt2,txt3,txt4,txt5]:
        st.write(j)

    st.write("## Thank you for Visiting \nProject by Nikhil J")
        

main()
