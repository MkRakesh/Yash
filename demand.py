import streamlit as st
import matplotlib.pyplot as plt
import joblib
import pickle
import statsmodels.api as sm

# Load the model
loaded_model = joblib.load('final_model.pkl')
fit = loaded_model.fit()
st.title('Demand Forecating')

input1 = st.number_input("Forecast Period:", min_value=0)

if input1 != 0 :
    # Use the predict method to make forecasts
    
    forecast_values = fit.predict(start=0, end=input1 - 1)
    plt.figure(figsize=(5,3)
    plt.ylabel('Forecast')
    plt.grid()
    forecast_values.plot()
    st.write('Demand Forecast')
    plt.grid()
    st.pyplot(plt)
