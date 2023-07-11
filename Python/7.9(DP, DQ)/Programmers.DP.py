# 프로그래머스 Level 3. 등굣길
def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 집 좌표니깐 문제에서 필요없기에 넘기기 
            if dp[i][j] == dp[1][1]:
                continue
                # 웅덩이를 만났을 때 -> 웅덩이 부분 계속 0으로 초기화해주기
            if [j, i] in puddles:
                dp[i][j] = 0
                
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return (dp[n][-1]) %  1000000007