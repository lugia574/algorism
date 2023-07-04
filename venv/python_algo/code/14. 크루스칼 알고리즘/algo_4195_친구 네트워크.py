# 이건 유니온파인드를 조금 개조한거임
# 이걸 이렇게 바꿔서 사용할줄을 알아야지 나중에 어려운 문제를 풀수 잇는거여
# 나는 처음에 그냥 단순히 딕셔너리 하나만을 어떻게 해볼까 했는데
# 그러면 안되고 두개를 써야함

import sys

def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a != b:
        parent[b] = a
        number[a] += number[b]

    print(number[a])

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        parent, number = {}, {}
        for _ in range(n):
            x, y = input().split()
            if x not in parent:
                parent[x] = x
                number[x] = 1
            if y not in parent:
                parent[y] = y
                number[y] = 1

            unionParent(x, y)

