#1
def solution(s):
    return s.isdecimal() and len(s) in (4, 6)

#2
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False
