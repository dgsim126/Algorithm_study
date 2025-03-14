# 숙소 배정이랑 똑같은 문제
# 1.
# ------------
# --------
# 2.
# ------
# ---------
from collections import deque

def solution(routes):
    routes = sorted(routes, key=lambda x: x[0])
    camera = deque([])
    num_camera = 0
    
    for i in routes:
        if not camera:
            camera.append(i)
        else:
            x, y = camera.popleft()
            if i[0] > y:
                camera.append(i)
                num_camera += 1
            else:
                if i[1] > y:
                    camera.append([i[0], y])
                else:
                    camera.append([i[0], i[1]])
    
    return num_camera + 1

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))