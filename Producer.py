import pandas as pd
from kafka import KafkaProducer,KafkaAdminClient
from time import sleep
from json import dumps
import json
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError
"""

# Step 1: Create Topic (optional if already exists)
admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])

try:
    topic = NewTopic(name='StockInfo', num_partitions=1, replication_factor=1)
    admin_client.create_topics(new_topics=[topic], validate_only=False)
    print(f"Topic '{'StockInfo'}' created.")
except TopicAlreadyExistsError:
    print(f"Topic '{'StockInfo'}' already exists.")
except Exception as e:
    print(f"Error creating topic: {e}")

"""
# Step 1: Load the forecasted prices and buy/sell signals
forecasted_prices_df = pd.read_csv('Forecasted_Prices.csv')  # Change path to your file
signals_df = pd.read_csv('Buy_sell_signals.csv')  # Change path to your file

# Step 2: Merge the two DataFrames on the date column
merged_df = pd.merge(forecasted_prices_df, signals_df, on='Date', how='inner')  


#Setting up the producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

# Convert merged DataFrame rows to JSON format and send each row through Kafka
for index, row in merged_df.iterrows():
    print("/n")
    print("New Stock Info:")
    print("/n")
    message = row.to_dict()  # Convert each row to a dictionary
    separator="/n"+"New Stcok Info"+"/n"
    producer.send("StockInfo", value=separator)
    producer.send('StockInfo', value=message)  # Change topic name as needed
    print(f"Sent message: {message}")
    sleep(2)






producer.flush()
print("All Data Sent Successfully")
