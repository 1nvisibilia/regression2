import math
import sys
import json
import random
import numpy as np
from kafka import KafkaConsumer
from stock_trainer import train_model

currency_name = sys.argv[1] if len(sys.argv) > 1 else "BTC-CAD"

consumer = KafkaConsumer(
    currency_name,
    auto_offset_reset="earliest",
    consumer_timeout_ms=1000,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")))

# each record in the kafka consumer is a 2 min interval, we will have
# 15 input args
# 5  outputs

# therefore, the final ML model should predict the stock trend of the next 10 minutes given the past
# data from half an hour ago

embedding = [-1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1, -1] # outputs

training_data = []
labels = []

for msg in consumer:
    embedding.pop(0)
    embedding.append(msg.value["price"])
    if (embedding[0] != -1):
        # add this embedding to the ml trainer
        training_data.append(embedding[:15])
        labels.append(embedding[15:])

print("processed " + str(len(training_data)) + " records in the topic")

random.shuffle(training_data)

train_x = training_data[:math.floor(len(training_data) * 0.8)]
val_x = training_data[math.floor(len(training_data) * 0.8):]
train_y = labels[:math.floor(len(labels) * 0.8)]
val_y = labels[math.floor(len(labels) * 0.8):]

train_model(
    np.array(train_x),
    np.array(train_y),
    np.array(val_x),
    np.array(val_y)
)