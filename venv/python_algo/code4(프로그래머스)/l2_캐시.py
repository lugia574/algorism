# 아니 설명을 해줘야지 시벌것이
# 18년도 문제라서 그런가?

def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0 : return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1

        else:
            if len(cache) == cacheSize: cache.pop(0)
            cache.append(city)
            answer += 5
    return answer

if __name__ == "__main__":
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    res = 50

    answer = solution(cacheSize, cities)
    print(res == answer, answer)

    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
    res = 21

    answer = solution(cacheSize, cities)
    print(res == answer, answer)

    cacheSize = 2
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    res = 60

    answer = solution(cacheSize, cities)
    print(res == answer, answer)

    cacheSize = 5
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
    res = 52
    answer = solution(cacheSize, cities)
    print(res == answer, answer)


    cacheSize = 2
    cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
    res = 16
    answer = solution(cacheSize, cities)
    print(res == answer, answer)


    cacheSize = 0
    cities= ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    res = 25
    answer = solution(cacheSize, cities)
    print(res == answer, answer)