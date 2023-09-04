# 음 그러니까 트리구조를 만들고 그걸 DFS 로 들어가서 순회를 돌리면 되는거 아닐까 생각은 하는데
# 그럼 막 아스키코드 값으로 조여야하나 근데 보면 값이 중복인게 있는데 어쩌지
# https://steadily-worked.tistory.com/807
# 이걸 보면 훨씬 쉽게 딕셔너리만으로 잘 해결함

import sys

def add(dic, arr):
    if len(arr) == 0:
        return

    if arr[0] not in dic:
        dic[arr[0]] = {}
    add(dic[arr[0]], arr[1:])


def printTree(dic, leng):
    for i in sorted(dic.keys()):
        print("--"*leng+i)
        printTree(dic[i],leng+1)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    a = [list(map(str, input().split())) for _ in range(n)]
    dic = {}

    for i in a:
        i = i[1:]
        add(dic, i)

    printTree(dic, 0)