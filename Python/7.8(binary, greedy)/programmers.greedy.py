# Level 1 체육복 
def solution(n, lost, reserve): 
    # 여벌의 체육복을 가져 온 학생이 체육복을 도난 당했을 경우
    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)
    
    cnt = 0
    for los in n_lost:
        if los-1 in n_reserve:
            n_reserve.remove(los-1)
            cnt += 1
        elif los+1 in n_reserve:
            n_reserve.remove(los+1)
            cnt += 1
    return (n-len(n_lost)) + cnt