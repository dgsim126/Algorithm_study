def solution(n, lost, reserve):
    clothes = [1 for _ in range(n)]

    for i in lost:
        clothes[i-1] -= 1
    for j in reserve:
        clothes[j-1] += 1

    for k in range(n):
        if clothes[k] == 0:
            if k > 0 and clothes[k-1] > 1:
                clothes[k-1] -= 1
                clothes[k] += 1
            elif k < n-1 and clothes[k+1] > 1:
                clothes[k+1] -= 1
                clothes[k] += 1

    count = 0
    for l in range(n):
        if clothes[l] != 0:
            count += 1

    return count