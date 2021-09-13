import yfinance as yf
import streamlit as st
import pandas as pd

st.write ("""
# Perubahan harga stock

memperlihatkan high, stock, open, dan close dari 

""")

# define ticker symbol
tickerSymbol = 'GOOGL' #nama stocknya
#get data pada ticker
tickerData = yf.Ticker(tickerSymbol)
#get ticker untuk riwayat
tickerDF = tickerData.history(period='id', start='2015-1-1', end='2021-10-9')
#untuk memperlihatkan riwayat adalah= open, high, low, close, volume, Dividends, splits

st.line_chart(tickerDF.High)
st.line_chart(tickerDF.Open)
st.line_chart(tickerDF.Close)