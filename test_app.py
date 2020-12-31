import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = "GOOGL"
# sacamos datos de yfinance
tickerData = yf.Ticker(tickerSymbol)
# generamos datos historicos
tickerDF = tickerData.history(period = 'id', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)