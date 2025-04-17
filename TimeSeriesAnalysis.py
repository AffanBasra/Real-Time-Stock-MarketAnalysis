import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.seasonal import seasonal_decompose

# Load your dataset (ensure 'Date' is a column in the CSV)
df = pd.read_csv("StockMarketData.csv")

# Convert 'Date' column to datetime and set it as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)




#for monthly seasonality (approx 30 days)
result = seasonal_decompose(df['Close'], model='multiplicative', period=30)


#Forecasting Data Points
trends = result.trend
seasonal = result.seasonal

print(df.sample(1))

df["Forecasted_Close_Price"]=trends
df.dropna(inplace=True)
print(df.head())
print(df[['Close','Forecasted_Close_Price']])

#Saving to a csv
df.to_csv('Forecasted_Prices.csv')
