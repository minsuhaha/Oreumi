class Car:
    wheel = 4
    window = 2
    # __ -> magic method!
    def __init__(self, people):
        self.people = people
        self.window = 2
        self.wheel = 4

    def brake(self):
        print(f'{self.people}(이)가 brake!')

    def accelrate(self):
        print("accelerate!")
    
my_car = Car('하민수')
my_car.brake()