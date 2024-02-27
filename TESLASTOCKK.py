import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Get historical data for TSLA for the past 10 years
tesla_data = yf.download('TSLA', start='2012-01-01', end='2022-01-01')

# Calculate moving averages
tesla_data['50-day MA'] = tesla_data['Close'].rolling(window=50).mean()
tesla_data['200-day MA'] = tesla_data['Close'].rolling(window=200).mean()

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=tesla_data.index,
    open=tesla_data['Open'],
    high=tesla_data['High'],
    low=tesla_data['Low'],
    close=tesla_data['Close'],
    increasing_line_color='green',
    decreasing_line_color='red',
    name='TSLA'
)])

# Add moving averages
fig.add_trace(go.Scatter(x=tesla_data.index, y=tesla_data['50-day MA'], mode='lines', line=dict(color='blue'), name='50-day MA'))
fig.add_trace(go.Scatter(x=tesla_data.index, y=tesla_data['200-day MA'], mode='lines', line=dict(color='red'), name='200-day MA'))

# Customize the chart
fig.update_layout(
    title='Tesla (TSLA) Stock Price with Moving Averages',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False
)

# Show the chart
fig.show()
#DEV BRANCH