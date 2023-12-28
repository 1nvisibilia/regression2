# regression
![project-logo](project-logo.png)
A set of real-time microservices for collecting and managing stock and cryptocurrency data with Apache Kafka and PyTorch

#### Quick Links
- [Architecture Overview](#architecture-overview)
    - [System Design](#system-design)
    - [Summary](#summary)
- [Step-by-step Instructions for Local Usages](#step-by-step-instructions-for-local-usages)
    - [Requirements](#requirements)
    - [Setup](#setup)
    - [Initialize Kafka Topics](#initialize-kafka-topics)
    - [Building the Base ML Model](#building-the-base-ml-model)
    - [Starting the Long-running Producer and Consumer Jobs](#starting-the-long-running-producer-and-consumer-jobs)
        - [Consumer](#consumer)
        - [Producer](#producer)

## Architecture Overview

### System Design

### Summary


## Step-by-step Instructions for Local Usages

### Requirements
1. Clone the respository
2. Have Apache Kafka installed
3. Have Python3 installed
<!-- 4. Have Docker Installed -->

### Setup
1. After installing Apache Kafka
2. Navigate into the `kafka_2.13-3.6.1` folder
3. Start up the ZooKeeper by running `bin/zookeeper-server-start.sh config/zookeeper.properties`
4. Start up the Kafka broker by running `bin/kafka-server-start.sh config/server.properties`
<!-- 5. docker stuffs... -->

*The instructions below should be executed within the /src directory*

### Initialize Kafka Topics
Run `python3 kafka_init.py` to create the Kafka topics for each of the stocks/cryptocurrencies listed
under `stock_names.py`

### Building the Base ML Model
Run `python3 train_model.py [currency-abbr]` to read all existing data from the `currency-abbr` Kafka
topic. `currency-abbr` defaults to BTC-CAD, see `stock_names.py` for examples.

The `train_model.py` program will save the model as the `model_data` file, and picks the file up for
future runs.

Run `train_model.py` repeatly to train and improve the model.

### Starting the Long-running Producer and Consumer Jobs

Both producer and consumer are real-time long-running jobs; they require manual termination.

#### Consumer
Running `python3 consumer.py [currency-abbr]` will start listening for new records in the Kafka
topic, and train the model upon getting new records.
#### Producer
Running `python3 producer.py` (on a different terminal) will periodically pull real-time stock data
from Yahoo's API. The full list of data it pulls are specified in `stock_names.py`.



<!--
bin/kafka-console-consumer.sh --topic BTC-CAD --from-beginning --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic BTC-CAD --bootstrap-server localhost:9092
-->
