import time

class AnomalyDetector:
    def __init__(self):
        pass

    def detect_anomaly(self, vitals):
        timestamp = time.time()
        if vitals["heart_rate"] < 50 or vitals["heart_rate"] > 120:
            return {"patient_id": vitals["patient_id"], "timestamp": timestamp, "metric": "heart_rate", "value": vitals["heart_rate"]}
        if vitals["blood_pressure"][0] < 90 or vitals["blood_pressure"][0] > 160:
            return {"patient_id": vitals["patient_id"], "timestamp": timestamp, "metric": "blood_pressure", "value": vitals["blood_pressure"]}
        if vitals["oxygen_saturation"] < 90:
            return {"patient_id": vitals["patient_id"], "timestamp": timestamp, "metric": "oxygen_saturation", "value": vitals["oxygen_saturation"]}
        return None