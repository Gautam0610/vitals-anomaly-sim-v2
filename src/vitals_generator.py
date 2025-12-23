import random

class VitalsGenerator:
    def __init__(self, patient_id):
        self.patient_id = patient_id

    def generate_vitals(self):
        heart_rate = random.randint(60, 100)
        blood_pressure = (random.randint(110, 140), random.randint(70, 90))
        oxygen_saturation = random.randint(95, 100)

        return {
            "patient_id": self.patient_id,
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "oxygen_saturation": oxygen_saturation
        }