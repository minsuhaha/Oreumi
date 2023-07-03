class HealthCheck:
    
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
     #  self.bmi = self.calculate_bmi()

    def check_health(self):
        bmi = self.calculate_bmi()
        self.bmi = bmi
        result = self.get_result(self.bmi)
        self.result = result

        print("=== 건강검진 결과 ===")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}")
        print(f"신장: {self.height}cm")
        print(f"체중: {self.weight}kg")
        print(f"BMI: {bmi:.2f}")
        print(f"결과: {result}")
  
    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return bmi

    def get_result(self, bmi):
        if bmi < 18.5:
            return "저체중"
        elif 18.5 <= bmi < 23:
            return "정상체중"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 25 <= bmi < 30:
            return "경도비만"
        else:
            return "고도비만"

    def backup_records(self):
        file_path = "Python/7.3(함수and클래스)/7.3(클래스)/context.txt"
        with open(file_path, 'w') as file:
            file.write(f"이름: {self.name}\n")
            file.write(f"나이: {self.age}\n")
            file.write(f"신장: {self.height}cm\n")
            file.write(f"체중: {self.weight}kg\n")
            file.write(f"BMI: {self.bmi}\n")
            file.write(f"결과: {self.result}\n")

# class instance 만들어주기

my_patient = HealthCheck(name="하민수", age=20, height=200, weight=100)
my_patient2 =  HealthCheck(name="하민수2", age=21, height=190, weight=100)
patients = [my_patient, my_patient2]

total_age = 0
for patient in patients:
    total_age += patient.age

print(total_age/len(patients))

# check_health를 먼저 실행을 해야지 backup_records에서 bmi랑 result를 넣어줄수있다!
my_patient.check_health()
my_patient.backup_records()








