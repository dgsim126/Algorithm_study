def solution(s):
    is_right = 0
    for i in s:
        if i == "(":
            is_right += 1
        else:
            is_right -= 1
        
        if is_right < 0:
            return False
    if is_right != 0:
        return False
    return True