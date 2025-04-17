from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'StockInfo',
     bootstrap_servers=['localhost:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

#Could set up for potential storage further
s3 = S3FileSystem()

for c in consumer:
    print(c.value)