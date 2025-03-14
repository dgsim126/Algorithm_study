def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return 5 * len(cities)
    else:
        for i in cities:
            i = i.upper()
            if len(cache) < cacheSize:
                if i in cache:
                    answer += 1
                    cache.remove(i)
                    cache.append(i)
                else:
                    answer += 5
                    cache.append(i)
            else:
                if i in cache:
                    answer += 1
                    cache.remove(i)
                    cache.append(i)
                else:
                    answer += 5
                    cache.pop(0)
                    cache.append(i)
    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))