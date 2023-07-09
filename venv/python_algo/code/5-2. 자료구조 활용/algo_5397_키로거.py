import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        typing = input().strip()
        left, right = [], []
        for typ in typing:
            if typ == '<':
                if left:
                    right.append(left.pop())
            elif typ == '>':
                if right:
                    left.append(right.pop())
            elif typ == '-':
                if left:
                    left.pop()
            else:
                left.append(typ)
        left.extend(reversed(right))
        print(''.join(left))