def solution(cacheSize, cities):
    cache = []
    time = 0

    if cacheSize == 0:
        return len(cities) * 5

    else:
        for city in cities:
            city = city.lower()

            if city in cache:
                cache.remove(city)
                cache.append(city)
                time += 1

            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5

        return time