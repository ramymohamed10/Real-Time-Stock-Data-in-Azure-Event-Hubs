import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('MSFT_stock_data.csv', index_col='Datetime', parse_dates=True)

# Plotting the closing prices
plt.figure(figsize=(10, 6))
plt.plot(df['Close'], label='Closing Price')
plt.title('MSFT Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Plotting high and low prices
plt.figure(figsize=(10, 6))
plt.plot(df['High'], label='High Price', color='green')
plt.plot(df['Low'], label='Low Price', color='red')
plt.title('MSFT High and Low Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the trading volume
plt.figure(figsize=(10, 6))
plt.bar(df.index, df['Volume'], width=0.005)
plt.title('MSFT Trading Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()
