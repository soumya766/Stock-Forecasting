# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:33:28 2023

@author: lenovo pc
"""

import streamlit as st
import psycopg2
import pandas as pd
import time
# from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta

today = datetime.date.today()

st.set_page_config(page_title="User Page", page_icon =":tada:", layout="wide")

# Initializing the connection
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

#------ Header Section ----------------
with st.container():
    st.title("Group 12 - Stock Forecasting")
    st.write("Participants: Aparna, Goutham, Soumya, Aadarsh, Ashish")
    # st.write("[Opening Money Control to check your portfolio valuation >>](https://www.moneycontrol.com/)")
    # st.subheader("Hi from Share Market :wave:")
    
      
# name=st.text_input("Dear User, please enter your firstname: ")
# st.write("Your name is : ", name)
# time.sleep(5)
        
# database connection #https://www.youtube.com/watch?v=yzHa1S3OO2s
conn = init_connection()
        
# def query run
@st.cache_data
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        result = cur.fetchall()
    return result


# Get the current datetime
now = datetime.date.today()

# select history
no_days = 240
delta = timedelta(days=no_days)

# get previous date
prev_date = now - delta
from_date = prev_date.strftime('%Y-%m-%d')
# from_date



st.write("******************Showing data from Daily Prediction Table **************************************")

daily_data_predict=run_query('select * from public.daily_data_predict_new')
upcoming_prediction_daily=pd.DataFrame(daily_data_predict)
upcoming_prediction_daily.columns=['date','close', 'close_prediction_future','close_prediction_historic', 'close_history']
# Set 'date' column as the index
upcoming_prediction_daily.set_index('date', inplace=True)
st.table(upcoming_prediction_daily)

st.write("******************Plotting Graph from Daily Prediction Table **************************************")

# Plotting Upcoming Close Price Prediction
fg, ax = plt.subplots(figsize=(10,5))
ax.plot(upcoming_prediction_daily.loc[from_date:, 'close_history'], label='Current Close Price')
ax.plot(upcoming_prediction_daily.loc[from_date:, 'close_prediction_historic'], label='Generated Close Price Historic')
ax.plot(upcoming_prediction_daily.loc[from_date:, 'close_prediction_future'], label='Predicted Close Price Future')
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
ax.set_xlabel('Date', size=15)
ax.set_ylabel('Stock Price', size=15)
ax.set_title('Upcoming Close Price Prediction', size=15)
ax.legend()
st.pyplot(fg)




st.write("******************Showing data from Monthly Prediction Table **************************************")

monthly_data_predict=run_query('select * from public.monthly_data_predict_new')
upcoming_prediction_monthly=pd.DataFrame(monthly_data_predict)
upcoming_prediction_monthly.columns=['date','close', 'close_prediction_future','close_prediction_historic', 'close_history']
# Set 'date' column as the index
upcoming_prediction_monthly.set_index('date', inplace=True)
st.table(upcoming_prediction_monthly)

st.write("******************Plotting Graph from Monthly Prediction Table **************************************")

# Plotting Upcoming Close Price Prediction
fg, ax = plt.subplots(figsize=(10,5))
ax.plot(upcoming_prediction_monthly.loc[from_date:, 'close_history'], label='Current Close Price')
ax.plot(upcoming_prediction_monthly.loc[from_date:, 'close_prediction_historic'], label='Generated Close Price Historic')
ax.plot(upcoming_prediction_monthly.loc[from_date:, 'close_prediction_future'], label='Predicted Close Price Future')
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
ax.set_xlabel('Date', size=15)
ax.set_ylabel('Stock Price', size=15)
ax.set_title('Upcoming Close Price Prediction', size=15)
ax.legend()
st.pyplot(fg)



    
    
    
    
    
             