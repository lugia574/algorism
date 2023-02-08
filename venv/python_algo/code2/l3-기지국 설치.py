


def solution(n, stations, w):
    answer = 0
    check = [0] * (n+1)
    cnt = 0

    for i in stations:
        for j in range(i-w, i+w+1):
            if 0 < j <= n:
                check[j] = 1

    for i in range(1, n+1):
        if check[i] == 0:
            cnt += 1
            check[i] = 1
            if cnt == w*2+1 or check[i+1] == 1 or i == n:
                cnt = 0
                answer += 1
        else:
            cnt == 0
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
    print(ans)
    print("True" if ans == answer else "False")

    ans2 = solution(N2, stations2, W2)
    print(ans2)
    print("True" if ans2 == answer2 else "Falsee")