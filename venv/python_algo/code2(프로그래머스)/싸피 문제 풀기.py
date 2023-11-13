arr = [(2, 2), (2, 2), (1, 2), (2, 1)]
n = len(arr)
answer = 0

def sol(start, s):
    dp = [0] * (n+1)


for i in range(n):
    l, x = arr[i]
    tank = l
    ok = True
    for j in range(i+1, n):
        if tank < x:
            ok = False
            break
        tank -= x
        tank += arr[j][0]
        x = arr[j][1]
    if ok:
        answer+= 1

print(answer)

# arr = [7, 7, 3, 3, 3, 2, 7, 6, 5, 1, 5, 7, 6, 6, 7, 6, 3]
# maxant = max(arr)
# answer = maxant
# arr.sort()
# for i in arr:
#     if i > (maxant - i):
#         answer += maxant - i
#     elif i < (maxant - i):
#         answer += i
# print(answer + maxant)

# cnt = [3, 1, 2, 6, ]
# answer = 0
# n =len(cnt)
# while True:
#     for i in range(n):
#         if cnt[i] < 3:
#             answer += 1
#
#
#
# print(answer)

# nset = set([2, 4, 5])
#
# for i in range(len(nset) ** 4):
#
#
# print(len(nset))

# from collections import deque
# a =[]
# b = []
# q = deque([24, 20, 18, 17, 29, 22, 16, 32, 7, 1, 14, 19, 10, 4, 8, 30])
# apre = 1
# bpre = 0
# while q:
#     num = 0
#     if q[0] > q[len(q)-1]:
#         num = q.popleft()
#     else:
#         num = q.pop()
#     if apre == 1:
#         a.append(num)
#         apre = 0
#         bpre = 1
#     else:
#         b.append(num)
#         apre = 1
#         bpre = 0
#
# print(sum(a))