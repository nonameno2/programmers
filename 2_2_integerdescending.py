#1
def solution(n):
    n = list(str(n))
    n.sort(reverse = True)
    return int("".join(n))

#2
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))