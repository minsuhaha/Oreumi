class Animal:
    def __init__(self, name):
        self.name = name

    # init 메소드를 꼭 안 만들어도 된다.
    def speak(self):
        print("동물이 소리를 냅니다")

class Dog(Animal):
    def __init__(self, name, color):
        # 생성자에서 이름 상속
        super().__init__(name)
        self.color = color

    # overiding(덮어쓰다) -> 상속받은 부모와 똑같은 메소드가 있음
    def speak(self):
        # super()를 통해 부모에 있는 메소드도 같이 상속받아 오버라이딩이 안됨
        super().speak()
        print("개가 짖습니다.")

my_dog = Dog('스트', '검은색')
print(my_dog.name)
print(my_dog.color)
my_dog.speak()