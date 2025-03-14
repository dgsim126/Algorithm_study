from itertools import permutations, combinations
import heapq
from collections import deque

# test= "fuck off"
# test= test.split(" ")
# print(test)
# test= "".join(test)
# print(test)

# test= [[1,21], [1,13], [4,5]]
# test.sort(key= lambda x : (x[0], x[1]))
# print(test)

test= [3,5,7,2,4,6,1]
# heapq.heapify(test)
# print(test)
# heapq.heappush(test, 0)
# print(test)
# heapq.heappop(test)
# print(test)

test= list(combinations(test, 2))
print(test)

test= deque(test)
print(test)
test.popleft()
print(test)

