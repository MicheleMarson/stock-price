# run -> streamlit run main.py
import streamlit as st
import pandas as pd
import yfinance as yf

# --markdown--
st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!
""")

# define the ticker symbol
ticker_symbol = "GOOGL"
# get data on this ticker
ticket_data = yf.Ticker(ticker_symbol)
# get the historical prices for the ticker
ticker_df = ticket_data.history(period="1d", start="2010-5-31", end="2020-5-31")
# Open   High    Low Close      Volume      Civident    Stock Splits

st.write("""
## Closing Price""")
st.line_chart(ticker_df.Close)

st.write("""
## Volume Price""")
st.line_chart(ticker_df.Volume)
