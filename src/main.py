import time
import random
import threading
from vitals_generator import VitalsGenerator
from anomaly_detector import AnomalyDetector
from kafka_producer import KafkaProducer

# TODO: Get Kafka topic from user
KAFKA_TOPIC = ""

NUM_PATIENTS = 5

def main():
    vitals_generators = [VitalsGenerator(patient_id=i) for i in range(NUM_PATIENTS)]
    anomaly_detector = AnomalyDetector()
    kafka_producer = KafkaProducer(topic=KAFKA_TOPIC)

    def generate_and_publish(generator):
        while True:
            vitals = generator.generate_vitals()
            anomaly = anomaly_detector.detect_anomaly(vitals)

            if anomaly:
                kafka_producer.send_message(anomaly)

            time.sleep(random.uniform(0.1, 0.5))

    threads = []
    for generator in vitals_generators:
        thread = threading.Thread(target=generate_and_publish, args=(generator,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()