from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)  # LRU 캐시로 사용할 deque
    total_time = 0

    for city in cities:
        city = city.lower()  

        if city in cache:
            # 캐시 히트
            cache.remove(city)  
            cache.append(city)
            total_time += 1
        else:
            # 캐시 미스
            cache.append(city) # 최대 큐의 크기를 정해놓았기에 가장 오래된(앞에 있는) 값 자동 삭제
            total_time += 5

    return total_time
