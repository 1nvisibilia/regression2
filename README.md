# regression
A set of real-time microservices for collecting and managing stock and cryptocurrency data with Apache Kafka and PyTorch


### Requirements
1. Clone the respository
2. Have Apache Kafka installed
<!-- 3. Have Docker Installed -->

### Setup
1. After installing Apache Kafka
2. Navigate into the `kafka_2.13-3.6.1` folder
3. Start up the ZooKeeper by running `bin/zookeeper-server-start.sh config/zookeeper.properties`
4. Start up the Kafka broker by running `bin/kafka-server-start.sh config/server.properties`
<!-- 5. docker stuffs... -->

### Initialize Kafka Topics
Run `python3 kafka_init.py` to create the Kafka topics for each of the stocks/cryptocurrencies listed
under `stock_names.py`

### Building the Base ML Model
Run `python3 train_model.py [currency-abbr]` to read all existing data from the `currency-abbr` Kafka
topic. The `train_model` program will save the model as the model_data file, and picks the file up for
future runs.

Run `train_model.py` repeatly to train and improve the model.

### Starting the Long-running Producer and Consumer Jobs
producer.py, consumer.py etc...


bin/kafka-console-consumer.sh --topic BTC-CAD --from-beginning --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic BTC-CAD --bootstrap-server localhost:9092