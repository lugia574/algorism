# 그래프 전위, 후위 순회임
# 와 이거 어떻게 하는지 까먹음 ㅋㅋ
# ㅋㅋㅋㅋㅋㅋ
# 이거 이진 트리 짜기도 어려운데?
# y 축을 기준으로 하는거 같긴한데
# https://wiselog.tistory.com/103
# https://www.youtube.com/watch?v=K6ZpR22qF1M

import sys
sys.setrecursionlimit(10 ** 6)

# Node 클래스 선언
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def __lt__(self, other):
        if (self.y == other.y):
            return self.x < other.x
        return self.y > other.y

# node 붙여주기 
# 왼쪽은 부모 x 가 더 크고 오른 쪽은 자식 x 가 더 큰것이 기준
def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)

def preorder(arr, node):
    if node is None:
        return
    arr.append(node.id)
    preorder(arr, node.left)
    preorder(arr, node.right)

def postorder(arr, node):
    if node is None:
        return
    postorder(arr, node.left)
    postorder(arr, node.right)
    arr.append(node.id)

def solution(nodeinfo):
    n = len(nodeinfo)
    nodeList = []
    for i in range(n):
        nodeList.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))

    nodeList.sort()
    root = nodeList[0]
    for i in range(1, n):
        addNode(root, nodeList[i])


    # 순회
    # 전위
    pre = []
    preorder(pre, root)
    # 후위
    post = []
    postorder(post, root)
    return [pre, post]

if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

    answer = solution(nodeinfo)
    print(result == answer)

