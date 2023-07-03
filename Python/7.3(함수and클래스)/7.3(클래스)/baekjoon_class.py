# 10825번 국영수
'''
import sys
n = int(sys.stdin.readline())
grades = [input().split() for _ in range(n)]

# sort 우선순위 순서대로 key:lambda x : (x[0], x[1], x[2], x[3])
grades.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for grade in grades:
    print(grade[0])
'''
class Car:
    def  __init__(self, model, car_type="electric"):
          self.model = model
          self.wheel = 4
          self.speed = 50
          self.car_type = car_type
    def brake(self):
          self.speed -= 50
    def accelerate(self):
          self.speed += 50

my_car = Car("Tesla")
my_car.accelerate() 
my_car.accelerate()
my_car.brake()
print(my_car.model, my_car.wheel, my_car.speed)

