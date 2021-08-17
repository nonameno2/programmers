# 1
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else: 
            answer += "박"    
    return answer

# 2
def solution(n):
    if n % 2 == 0:
        return ("수박" * (n // 2))
    else:
        return ("수박" * (n // 2) + "수")
