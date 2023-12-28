from time import sleep
import json
import stock_names
import data_fetcher
from kafka import KafkaProducer

# initializer producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer = lambda v: json.dumps(v).encode("utf-8"))

# cron producer job that pulls real-time data from Yahoo API every 2 minutes
while True:
    for name_abbr in stock_names.stock_name_symbols:
        # only get the last record
        data = data_fetcher.fetch_stock(name_abbr, "1d")[-1]
        producer.send(name_abbr, data)
        print("pushed a record in: " + name_abbr + ".")
    sleep(60 * 2) # 2 minutes
