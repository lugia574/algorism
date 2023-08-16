import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    dic = dict()
    n = 0
    while True:
        tree = input().rstrip()
        if tree == '':
            break
        n += 1
        if tree in dic:
            dic[tree] += 1
        else:
            dic[tree] = 1

    cartegory = list(dic.keys())
    cartegory.sort()


    for x in cartegory:
        res = (dic[x] / n * 100)
        print('%s %.4f' %(x, res))


