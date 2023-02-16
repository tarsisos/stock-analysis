import streamlit as st

import pandas_datareader.data as web

import plotly.graph_objects as go
from PIL import Image

import yfinance as yf
yf.pdr_override()

#Setting page title and icon
st.set_page_config(
  page_title='Market Analysis',
  page_icon= Image.open('./content/candlestick.png'),
)

st.sidebar.title('Menu')

# Creating a dictionary with companies tickers and name
Company_Ticker = {
  'MSFT': 'Microsoft',
  'IBM': 'IBM',
  'AAPL': 'Apple',
  'GOOGL': 'Alphabet (Google)'
}

Select_Company = st.sidebar.selectbox('Select company', Company_Ticker.keys())


# This range selects the number of months you want to analyze.
# In case of selection is 0 (zero), will inform the conrespond day.
Date_Range = st.sidebar.slider('Month period:', 0, 12, 1, key='Select_bar')

# Convert int Date_Range to String, concatenates with 'mo' so
# The YFinance API recognize that the priod we want is the Month
Date_Range_Selection = str(Date_Range) + 'mo'

# Create two columns:
# -> Left: candlestick graphic and stock registries with 90% of space
# -> Right: company logo with 10% of space
left, right = st.columns([0.9, 0.1])

# List with companies logos
Images = [
  'https://cdn-icons-png.flaticon.com/512/732/732221.png',
  'https://cdn-icons-png.flaticon.com/512/882/882727.png',
  'https://cdn-icons-png.flaticon.com/512/179/179309.png',
  'https://cdn-icons-png.flaticon.com/512/300/300221.png'
]

# Title of the dashboard
Title = f'Economic Analysis {str(Select_Company)}'
left.title(Title)

# Condition to show the company logo
if Select_Company == 'MSFT':
  right.image( Images[0], width=100)
elif Select_Company == 'IBM':
  right.image( Images[1], width=100)
elif Select_Company == 'AAPL':
  right.image( Images[2], width=100)
else:
  right.image( Images[3], width=100)

# Collects data from Yahoo! Finance API
Data = web.get_data_yahoo(Select_Company, period = Date_Range_Selection)


Candlestick_Graphic = go.Figure(
  data=[
    go.Candlestick(
      x = Data.index,
      open = Data['Open'],
      high = Data['High'],
      low = Data['Low'],
      close = Data['Close']
    )
  ]
)

Candlestick_Graphic.update_layout(
  xaxis_rangeslider_visible = False,
  title = f'Stock Analysis from {Company_Ticker.get(Select_Company)}',
  xaxis_title = 'Period',
  yaxis_title = 'Price'
)

st.plotly_chart(Candlestick_Graphic)

if st.checkbox('Show data as table'):
  st.subheader('Registries table')
  st.write(Data)

st.sidebar.subheader(
  'Made by: Társis Santos')

st.sidebar.markdown(
  '[![Title](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/tarsisos/)',
  unsafe_allow_html=True
  )

st.sidebar.write('''
  Feito durante a Semana de Eventos com Python nos dias 07, 08 e 09 de Fevereiro de 2023.\n
  Instrutor: Odemir Depieri Jr.
'''
)