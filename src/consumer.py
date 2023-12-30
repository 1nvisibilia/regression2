import sys
import json
import random
import math
from stock_trainer import train_model
import numpy as np
from kafka import KafkaConsumer

currency_name = sys.argv[1] if len(sys.argv) > 1 else "BTC-CAD"
non_wait_consumer = KafkaConsumer(
    currency_name,
    auto_offset_reset="earliest",
    consumer_timeout_ms=1000,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")))

embedding = [-1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1, -1] # outputs
raw_data = []

for msg in non_wait_consumer:
    embedding.pop(0)
    embedding.append(msg.value["price"])
    if (embedding[0] != -1):
        # add this embedding to the ml trainer
        raw_data.append(embedding.copy())

del non_wait_consumer

consumer = KafkaConsumer(
    currency_name,
    value_deserializer=lambda m: json.loads(m.decode("utf-8")))

for msg in consumer:
    print("received a record in:", currency_name)
    # update the newest value
    embedding.pop(0)
    embedding.append(msg.value["price"])
    raw_data.append(embedding)

    # randomize data
    random.shuffle(raw_data)

    training_data = [entry[:15] for entry in raw_data]
    labels = [entry[15:] for entry in raw_data]

    train_x = training_data[:math.floor(len(training_data) * 0.8)]
    val_x = training_data[math.floor(len(training_data) * 0.8):]
    train_y = labels[:math.floor(len(labels) * 0.8)]
    val_y = labels[math.floor(len(labels) * 0.8):]

    train_model(
        np.array(train_x),
        np.array(train_y),
        np.array(val_x),
        np.array(val_y),
        1
    )