# 백준 25501번. 재귀의 귀재 
'''
def recursion(s, l, r):
    if l >= r: 
       return 1, l+1
    elif s[l] != s[r]: 
       return 0, l+1
    else: 
      # left는 +1, right -1 해줌으로써 다시 비교 ㄱㄱ
      return recursion(s, l+1, r-1)

def isPalindrome(s):
    # l = 0, r = len(s) - 1
    return recursion(s, 0, len(s)-1)

n = int(input())
for i in range(n):
  s = input()
  answer = isPalindrome(s)
  print(answer[0], answer[1])
'''

# 11729번. 하노이의 탑   -> 이런문제 꿀팁 : 작은 수의 예시부터 스스로 그려보자!
# 바로 직전 내용이 반복된다!!..
# 점심시간에 다시 복습해보자
def hanoi(start, middle, end, n):
   if n == 1:
      print(start, end)
   else:
      hanoi(start, end, middle, n-1)
      print(start, end)
      hanoi(middle, start, end, n-1)
      
n = int(input())
print(2*n + 1)
hanoi(1, 2, 3, n)

