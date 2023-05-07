# https://wiselog.tistory.com/118
# 결국 못풀었으니까 하나하나 주석을 달아보자
# 나는 받은 배열을 재 가공해서 그래프화했는데
# 요것은 그냥 쌩으로 씀
# dfs 시작할때 kick 할 노드 넘버랑 배열을 넣어주고 시작
# 해당 노드 넘버에 있는 간선은 -2 로 아예 삭제 (-1 은 root 노드 표시니까)
# 배열 전체를 탐색하며, 방금 삭제한 인덱스를 부모노드로 가지는 노드를 찾아 dfs함수를 재귀호출
# 재귀가 끝나면 삭제될 노드들은 전부 -2로 갱신되어있으므로,
# -2가 아니면서, 다른 노드의 부모노드도 아닌 원소(leaf 노드)를 찾을 때마다 count를 1씩 늘린다.
# 이럼 root 노드 딱 하나만 남아 있어도 카운터 해줌
# 난 이렇게 생각 절대 못할꺼 같은데

import sys

def dfs(num, arr, n):
    arr[num] = -2
    for i in range(n):
        if num == arr[i]:
            dfs(i, arr, n)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    count = 0

    dfs(k, arr, n)
    for i in range(n):
        if arr[i] != -2 and i not in arr:
            count += 1
    print(count)


# 2
# -1 0
# 1
# (루트노드 단 하나만 남음)
#
# 정답 : 1
#
# 9
# -1 0 0 5 2 4 4 6 6
# 4
#
# 정답 : 2 (루트 노드에 연결된 1 and 2 가 리프 노드가 됨)