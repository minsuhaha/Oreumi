# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     # 영역의 넓이
#     def area(self):
#         return self.width * self.height

# rectangle = Rectangle(4,5)
# print(f"너비 : {rectangle.width} 높이 : {rectangle.height}")
# print(rectangle.area())

class Animal:
    def sound_play(self):
        pass

class Cat(Animal):
    # default값을 지정해주려면 매개변수의 가장 뒤로
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f'{self.name} : {self.sound}*2'
    
class Dog(Animal):
    def __init__(self, sound, name, legs=4):
        self.legs = legs
        self.sound = sound
        self.name = name

    def sound_play(self):
        return f'{self.name} : {self.sound}*2'

animals = [Cat(name = '르미', sound='Meow'), Dog(name = '스트', sound='Bark')]
for animal in animals:
    print(animal.sound_play())
