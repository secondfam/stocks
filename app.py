import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st


start = '2014-09-16'
end = '2023-11-09'

st.title('Stock Trend Prediction')


user_input = st.text_input('Enter Stock Ticker', 'BTC_USD')
df = yf.download(user_input, 'yahoo', start=start, end=end)


#Describing Data
st.subheader('Data from 2014 - 2023')
st.write(df.describe())