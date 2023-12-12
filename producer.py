import requests
from kafka import KafkaProducer, KafkaAdminClient
from kafka.admin import NewTopic


producer = KafkaProducer(bootstrap_servers='localhost:9092')
admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')


# conf = {'bootstrap.servers': "host1:9092,host2:9092",
#         'client.id': socket.gethostname()}

# producer = Producer(conf)

admin_client.create_topics(new_topics=[NewTopic(name="BTC-CAD",num_partitions=1, replication_factor=1)])


base_url = "https://query1.finance.yahoo.com/v7/finance/spark?"

options = {
    "symbols": "BTC-CAD",
    "range": "1mo"
}

headers = {
    "User-Agent": "..."
}

def generateUrl():
    params = ""
    for key in options:
        params += (key + "=" + options[key] + "&")
    return base_url + params

data = requests.get(generateUrl(), headers=headers).json()

timestamps = data["spark"]["result"][0]["response"][0]["timestamp"]
prices = data["spark"]["result"][0]["response"][0]["indicators"]["quote"][0]["close"]

series = list(zip(timestamps, prices))
