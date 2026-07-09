import heapq

class Patient:
    def __init__(self, id, name, disease, type, department):
        self.id = id
        self.name = name
        self.disease = disease
        self.type = type
        self.department = department

    def patient_info(self):
        print(f"Patient ID: {self.id}, Name: {self.name}, Disease: {self.disease}, Type: {self.type}, Department: {self.department}")

patient1 = Patient(1, "Justin", "Flu", "Inpatient", "General Medicine")
patient2 = Patient(2, "Anna", "Diabetes", "Outpatient", "Endocrinology")
patient3 = Patient(3, "Mikki", "Hypertension", "Inpatient", "Cardiology")
patient4 = Patient(4, "Eldho Antu", "Mental Illness", "Outpatient", "Psychiatry")

patient = []  

heapq.heappush(patient, (2, patient1))
heapq.heappush(patient, (1, patient4))
heapq.heappush(patient, (3, patient2))
heapq.heappush(patient, (4, patient3))


while patient:
    priority, p = heapq.heappop(patient)
    print(f"Priority: {priority} -> ", end="")
    p.patient_info()