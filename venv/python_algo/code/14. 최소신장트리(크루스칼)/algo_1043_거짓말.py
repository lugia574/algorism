# 처음에는 그냥 2중 포문 돌리면서 해당 배열 있는가 확인하는 문제라고 생각했는데

# 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 
# 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 
# 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.

# 즉 유니파인드 문제임
# 진실을 알고 있는 놈들 부모는 0 으로 표시하고
# 각 파티 별 애들 전부를 unionParent 해버려
# 그럼 이제 남는 이제 부모가 0 이 아닌 애들이 있거 그 파티 수가 구라 쌉가능 수라는거

import sys

def witness(arr):
    for x in arr:
        if parent[x] == 0:
            return True
    return False

def getParent(a):
    if parent[a] != a:
        parent[a] = getParent(parent[a])
    return parent[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parent = [i for i in range(0, n+1)]
    for i in list(map(int, input().split()))[1:]:
        if i == 0: continue
        parent[i] = 0

    parties = [list(map(int, input().split())) for _ in range(m)]

    length = len(parties)

    for party in parties:
        for i in range(party[0]):
            if i > 0:
                unionParent(party[i], party[i+1])

    for i in range(1, n+1):
        getParent(i)

    for party in parties:
        if witness(party[1:]):
            length -= 1

    #print(parent)
    print(length)