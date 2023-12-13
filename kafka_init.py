from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic
from time import sleep
import stock_names
import data_fetcher
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer = lambda v: json.dumps(v).encode('utf-8'))

admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')

# remove existing topics
existing_topics = admin_client.list_topics()
for topic_name in existing_topics:
    if (topic_name in stock_names.stock_name_symbols):
        admin_client.delete_topics(topics=[topic_name])
        print(topic_name + " has been deleted.")

# wait for a period of time, for kafka to finish deletion
sleep(2)

# create topics
for name_abbr in stock_names.stock_name_symbols:
    admin_client.create_topics(new_topics=[
        NewTopic(name=name_abbr,num_partitions=1, replication_factor=1)
    ])
    print("topic " + name_abbr + " created.")

# start off with one month of data
for name_abbr in stock_names.stock_name_symbols:
    data = data_fetcher.fetch_stock(name_abbr, "1mo")
    for record in data:
        producer.send(name_abbr, record)
    print("initialized data in: " + name_abbr + ".")
