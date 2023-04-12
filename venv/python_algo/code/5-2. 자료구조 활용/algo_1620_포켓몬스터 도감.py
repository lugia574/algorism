import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    wikiWords = {}
    wikiNums = {}
    for i in range(1, n + 1):
        name = input().strip()
        wikiWords[name] = i
        wikiNums[i] = name

    for j in range(m):
        order = input().strip()
        if order.isalpha():
            print(wikiWords.get(order))
        else:
            order = int(order)
            print(wikiNums.get(order))