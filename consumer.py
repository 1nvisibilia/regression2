import sys
import json
from kafka import KafkaConsumer

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