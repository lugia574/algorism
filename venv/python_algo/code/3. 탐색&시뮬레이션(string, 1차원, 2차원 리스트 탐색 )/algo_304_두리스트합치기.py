# 두 리스트 합치기
# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
# 그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
# 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
# 세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
# 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
# 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
# ▣ 출력설명
# 오름차순으로 정렬된 리스트를 출력합니다.
# ▣ 입력예제 1
# 3
# 1 3 5
# 5
# 2 3 6 7 9
# ▣ 출력예제 1
# # 1 2 3 3 5 6 7 9

n = int(input())
numListA = list(map(int,input().split()))
m = int(input())
numListB = list(map(int, input().split()))
p1 = p2 = 0
res = []

while p1<n and p2<m:
    if numListA[p1] <= numListB[p2]:
        res.append(numListA[p1])
        p1 += 1
    else :
        res.append(numListB[p2])
        p2 += 2
if p1 < n:
    res = res + numListA[p1:]
if p2 < m :
    res = res + numListB[p2:]

for x in numListA:
    print(x, end=" ")