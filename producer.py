import requests
from kafka import KafkaProducer, KafkaAdminClient
import stock_names

producer = KafkaProducer(bootstrap_servers='localhost:9092')
admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
