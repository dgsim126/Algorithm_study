'''
전에 풀었던 얼음판 위에서 미끄러지는 문제와 비슷
- bfs로 풀면 될 거 같음
- 현재 내 위치에서 사방으로 움직이며 도착하는지를 확인
- 이전 이동 방향(left)을 기억하고 현재 위치에서 이동할 수 있는 방향이 아까 왔던 방향 하나라면(left, right) 그떄 실패
'''
from collections import deque

def solution(n, m, map):

