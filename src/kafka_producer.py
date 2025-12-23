from kafka import KafkaProducer
import json

class KafkaProducer:
    def __init__(self, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],  # Replace with your Kafka broker address
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def send_message(self, message):
        self.producer.send(self.topic, value=message)
        self.producer.flush()