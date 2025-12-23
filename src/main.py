import time
import random
import threading
import logging
from vitals_generator import VitalsGenerator
from anomaly_detector import AnomalyDetector
from kafka_producer import KafkaProducer

KAFKA_TOPIC = "vitals_anomalies"
NUM_PATIENTS = 50

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    vitals_generators = [VitalsGenerator(patient_id=i) for i in range(NUM_PATIENTS)]
    anomaly_detector = AnomalyDetector()
    kafka_producer = KafkaProducer(topic=KAFKA_TOPIC)

    def generate_and_publish(generator):
        while True:
            try:
                vitals = generator.generate_vitals()
                anomaly = anomaly_detector.detect_anomaly(vitals)

                if anomaly:
                    kafka_producer.send_message(anomaly)
                    logging.info(f"Anomaly detected for patient {generator.patient_id}: {anomaly}")

                time.sleep(random.uniform(0.1, 0.5))

            except Exception as e:
                logging.error(f"Error in thread for patient {generator.patient_id}: {e}")
                break

    threads = []
    for generator in vitals_generators:
        thread = threading.Thread(target=generate_and_publish, args=(generator,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()