import pandas as pd

# Load your stock market data
df = pd.read_csv('StockMarketData.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

#Basic Info
print(df.head())
df=df.dropna()
print(df.info())

#Upper and Lower Bollinger Bands
#window size=30 for monthly analysis
df['Rolling Mean']=df['Close'].rolling(30).mean()
df['Rolling Std Dev']=df['Close'].rolling(30).std()
df['Upper Band']=df['Rolling Mean'] + 2*df['Rolling Std Dev']
df['Lower Band']=df['Rolling Mean'] - 2*df['Rolling Std Dev']


#Generating buy and sell signals based on Bollinger Bnads
df['Buy Signal'] = (df['Close'] < df['Lower Band'])
df['Sell Signal'] = (df['Close'] > df['Upper Band'])

#Using drop na to remove irrleveant rows
df.dropna(inplace=True)

df.to_csv('Buy_sell_signals.csv')

#Converting random samples to json before streaming through kafka producer
print(df.sample(1).to_dict())

