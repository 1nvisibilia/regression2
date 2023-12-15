import sys
import json
from kafka import KafkaConsumer

currency_name = sys.argv[1] or "BTC-CAD"

consumer = KafkaConsumer(
    currency_name,
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")))

# each record in the kafka consumer is a 15 min interval, we will have
# - 3 * 4 = 12 input args
# - 1 * 4 = 4  outputs

# therefore, the final ML model should predict the stock trend of the next hour given the past data from
# 3 hours ago

embedding = [-1, -1, -1, -1, -1, -1, -1, -1, # input args
             -1, -1, -1, -1]                 # outputs

for msg in consumer:
    embedding.pop(0)
    embedding.append(msg)
    print(embedding)
    if (embedding[0] != -1):
        # send this embedding to the ml trainer
        pass
