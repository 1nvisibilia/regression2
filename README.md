# regression
A set of real-time microservices for collecting and managing stock and cryptocurrency data with Apache Kafka and PyTorch


### Requirements
1. Clone the respository
2. Have Apache Kafka installed
3. Have Docker Installed

### Setup
1. After installing Apache Kafka
    a. Navigate into the `kafka_2.13-3.6.1` folder
    b. Start up the ZooKeeper by running `bin/zookeeper-server-start.sh config/zookeeper.properties`
    c. Start up the Kafka broker by running `bin/kafka-server-start.sh config/server.properties`
2. docker stuffs...