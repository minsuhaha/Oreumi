fav_fruits = ["사과", "수박", "배"]
mom_fruits = ['멜론', '수박', '배', '딸기']
eat_list = []

# 엄마가 사온 과일에서 내가 좋아하는 과일만 먹고싶다?
for fruit in mom_fruits:
    if fruit in fav_fruits:
        print("먹는다")
        eat_list.append(fruit)
    else:
        print("먹지 않는다")
print(eat_list)

# fruit가 fruits배열 안에 있다면? 
fruit = "수박"
if fruit in fav_fruits:
    print("내가 좋아하는 과일이다!")
else:
    print("별로 좋아하지 않는다..")