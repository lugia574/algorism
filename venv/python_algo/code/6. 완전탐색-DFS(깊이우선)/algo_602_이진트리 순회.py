# 이진트리 순회(깊이우선탐색)
# 이진트리를 전위순회와 후위순회를 연습해보세요
#               1
#       2               3
#   4       5       6           7
# 전위순회 출력 : 1 2 4 5 3 6 7 >> 부모/ 왼쪽/ 오른쪽
# 중위순회 출력 : 4 2 5 1 6 3 7 >> 왼쪽/ 부모/ 오른쪽
# 후위순회 출력 : 4 5 2 6 7 3 1 >> 왼쪽/ 오른쪽/ 부모

def preOrder (num):
    if num > 7:
        return
    print(num, end=" ")
    posetOrder(num*2)
    posetOrder(num*2+1)


def inOrder(num):
    if num > 7:
        return
    posetOrder(num*2)
    print(num, end=" ")
    posetOrder(num*2+1)

def posetOrder(num):
    if num > 7:
        return
    posetOrder(num*2)
    posetOrder(num*2+1)
    print(num, end=" ")


if __name__ == "__main__":
    print("전위순회 출력 :", end=" ")
    preOrder(1)
    print()
    print("중위순회 출력:", end=" ")
    inOrder(1)
    print()
    print("후위순회 출력:", end=" ")
    posetOrder(1)
    print()