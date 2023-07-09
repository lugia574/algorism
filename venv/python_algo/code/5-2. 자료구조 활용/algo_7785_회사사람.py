import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    company = {}
    for _ in range(n):
        name, staus = map(str, input().split())
        if name not in company:
            company[name] = True
        else:
            if staus == "enter":
                company[name] = True
            else:
                company[name] = False
    arr = []
    for k in company.keys():
        if company[k]:
            arr.append(k)

    arr.sort(reverse=True)
    for i in arr:
        print(i)