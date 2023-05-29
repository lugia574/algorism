import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    strArr = input().rstrip()
    stack = []
    tag = False
    res = ''

    for s in strArr:
        if s == " ":
            while stack:
                res += stack.pop()
            res += s
        elif s == "<":
            while stack:
                res += stack.pop()
            tag = True
            res += s
        elif s == ">":
            tag = False
            res += s
        elif tag:
            res += s
        else:
            stack.append(s)

    while stack:
        res += stack.pop()

    print(res)
