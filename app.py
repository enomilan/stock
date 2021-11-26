import streamlit as st
import yfinance as yf
import pandas as pd


ticker1 = 'AMZN'
ticker2 = 'AAPL'
ticker3 = 'GME'

tickerData = yf.Ticker(ticker1)
tickerData = yf.Ticker(ticker2)
tickerData = yf.Ticker(ticker3)