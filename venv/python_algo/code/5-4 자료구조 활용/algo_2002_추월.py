# 먼 나는 q 구조로 pop 갈기고 그래야하 하나 했는데
# 그냥 2중 포문으로 완전탐색 갈겨버리네
# out[i] 인덱스가 좀 더 큰 경우(더 느리다) 하나 발견되면 무조건 추월이니까 cnt 해주고 break
# n 도 10_000 밖에 안되니 N^2 해도 백만밖에 안돼 거기다 시간 제한 2초임 존나 널널함
# 에휴 진짜 이젠 이 쉬운것도 못푼다
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    answer = 0
    enter, out = dict(), []
    for i in range(N):
        car = input()
        enter[car] = i
    for _ in range(N):
        car = input()
        out.append(car)

    for i in range(N-1):
        for j in range(i+1, N):
            if enter[out[i]] > enter[out[j]]:
                answer += 1
                break
    print(answer)



# 4
# ZG431SN
# ZG5080K
# ST123D
# ZG206A
# ZG206A
# ZG5080K
# ZG431SN
# ST123D