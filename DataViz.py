import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

# Load your dataset (ensure 'Date' is a column in the CSV)
df = pd.read_csv("StockMarketData.csv")

# Convert 'Date' column to datetime and set it as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Visualize closing prices
df['Close'].plot(figsize=(12, 5), title='Stock Closing Prices')
plt.show()



#for monthly seasonality (approx 30 days)
result = seasonal_decompose(df['Close'], model='multiplicative', period=30)

# Plot decomposition
result.plot()
plt.suptitle("Seasonal Decomposition", fontsize=16)
plt.tight_layout()
plt.show()


#Forecasting Data Points
trends = result.trend
seasonal = result.seasonal

print(df.sample(1))

