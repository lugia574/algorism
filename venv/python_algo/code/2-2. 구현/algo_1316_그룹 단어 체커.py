import sys

def groupChecker(st):
    dic = []
    pre = st[0]
    for x in st[1:]:
        if pre == x:
            continue
        if x in dic:
            return False
        dic.append(pre)
        pre = x

    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    answer = 0
    for _ in range(n):
        st = input().strip()
        if groupChecker(st):
            answer += 1

    print(answer)
