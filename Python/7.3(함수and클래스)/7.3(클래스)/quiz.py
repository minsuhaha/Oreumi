# 상속 버전
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1

class Magician(Player):
    def skill(self):
        print("Magician skill {} activate!".format(self.level))

    def level_up(self):
        self.level += 1
        print("magician level up!!!")

class Warrior(Player):
    def skill(self):
        print("warrior skill {} activate!".format(self.level))

    def level_up(self):
        self.level += 1
        print("warrior level up!!!")
        

oreumi_1 = Magician('est')
oreumi_2 = Warrior('soft')

oreumi_1.skill()
oreumi_2.skill()
print("{}, now level = {}".format(oreumi_1.name, oreumi_1.level))
oreumi_1.level_up()
print("{}, now level = {}".format(oreumi_1.name, oreumi_1.level))
oreumi_1.skill()

# 상속 안하는 버전
class magician:
 
    def __init__(self, name):
        self.name = name
        self.level = 1

    def skill(self):
        print(f"magician skill {self.level} activate!")

    def level_up(self):
        self.level += 1
        print('magician level up!!!')

class worrior:

    def __init__(self, name):
        self.name = name
        self.level = 1

    def skill(self):
        print(f"worrior skill {self.level} activate!")

    def level_up(self):
        self.level += 1
        print('worrior level up!!!')

oreumi_1 = magician('est')
oreumi_2 = worrior('soft')

oreumi_1.skill()
oreumi_2.skill()
print("{}, now level = {}".format(oreumi_1.name, oreumi_1.level))
oreumi_1.level_up()
print("{}, now level = {}".format(oreumi_1.name, oreumi_1.level))
oreumi_1.skill()