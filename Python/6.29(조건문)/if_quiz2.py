# # 알람 문제 (원래 알람 시간보다 45분을 작게 해주는 문제) 
# # 시간 : h, 분 : m
# h, m = map(int, input().split())
# if m < 45:
#     # 자정 일 경우
#     if h == 0:
#         h = 23
#         m += 15
#     # 자정이 아닐경우
#     else:
#         h -= 1
#         m += 15
# else:
#     m -= 45
# print(h, m)   
'''
up and down  문제입니다 ~!
답을 하나 정하시고, 입력을 받으면서 해당 단계의 범위를 출력해 보는 것입니다.

입력값이 정답일 경우 : "정답" 과 함께 break를 이용해 프로그램 멈춤 
입력값이 정답 보다 클 경우: "그것보다 작습니다 "와 함께 " 현재 범위는 "20~50 "입니다. 
입력값이 정답 보다 작을 경우: "그것보다 큽니다"와 함께 " 현재 범위는 "29~50"입니다. 
범위에 없을 경우: "범위에 없습니다" 
를 출력하는 것입니다. 

오늘 배운 반복문 제어와 플래그, min, max찾기를 이용하시면 됩니다 ~!
'''
answer = 40
max = 50
min = 0
while True:
    n = int(input("숫자를 입력해주세요: "))
    if answer == n:
        print("정답")
        break
    elif answer < n:
        max = n
        print(f"less than {max}")
        print(f"현재 범위는 {min} ~ {max} 입니다.")
    else: 
        min = n
        print(f"greater than {min}")
        print(f"현재 범위는 {min} ~ {max} 입니다.")


