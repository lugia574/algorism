# 뭔소리지 이해가 안감
# https://jennnn.tistory.com/82

import math
def solution(n, stations, w):
    answer = 0
    cnt = 0
    dist = []

    for i in range(1, len(stations)):
        dist.append((stations[i] - w - 1) - (stations[i - 1] + w))

    dist.append(stations[0] - w - 1)
    dist.append(n - (stations[-1] + w))

    print(stations)
    print(dist)

    for i in dist:
        if i <= 0:
            continue
        else:
            print("================")
            print(i)
            print(i / (2 * w + 1))
            answer += math.ceil(i / (2 * w + 1))
    return answer

if __name__ == "__main__":
    N = 11
    stations = [4, 11]
    W = 1
    answer = 3

    N2 = 16
    stations2 = [9]
    W2 = 2
    answer2 = 3
    
    ans = solution(N, stations, W)
    # print(ans)
    print("True" if ans == answer else "False")

    ans2 = solution(N2, stations2, W2)
    # print(ans2)
    print("True" if ans2 == answer2 else "Falsee")