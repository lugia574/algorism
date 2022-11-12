# print("hello world!")
# a= 2
# b= 2
#
# print(a, b)

# a1,b2 = input("요호호ㅗ").split()

# a1, b2 = map(int,input("끼야앗호").split())
#
# for i in range(10 , 0, -1):
#     print(i)

# for i in range(1, 11):
#     if i%2 == 1:
#         continue
#     print(i)
#
# else:
#     print("끝났습니당")
#
# a = [[0]*3]*3
# print(a)
# a[0][1] = 1
# a[0][2] = 2
#
# for i in range(3):
#     for j in range(3):
#         print(a[i][j], end=" ")
#     print()
#
# print(a[1][2])
#
# for i in range (1, 10):
#     print(i)
#
# testList = [1,2,3,4,5]
# testList.pop()
# print(testList)
#
# testList.pop(0)
# print(testList)

# testList = [[0]*5 for i in range(5)]
#
#
# for i in range(5):
#     for j in range(5):
#         testList[i][j] = int(input())

# N = int(input())
#
# arr = [0 for _ in range(N)]
#
# for i in range(N):
#     arr[i] = list(map(int, input().split()))
#
# print(arr[:][0])

def fnc(arr, n):
    res = False
    numArr = [0] * (n+1)

    for x in arr:
        numArr[x] = 1

    for i in range(1, n + 1):
        if numArr[i] == 0:
            if i == k:
                return res
            else:
                break
    resArr.append(arr)
    res = True
    return res



n = int(input())
k = int(input())
arr = list(map(int,input().split(",")))
resArr = []
cnt = 0
for i in range(n):
    for j in range(i+1,n+1):
        res = fnc(arr[i:j],n)
        if res == True:
            cnt += 1
print(cnt)
print(resArr)

#
# 10
# 4
# 8,9,4,6,5,1,2,3,10,7
#
# 7
# 3
# 7,5,1,4,6,2,3
#
# 4
# 3
# 3,2,1,4
#
# 15
# 6
# 7,8,5,14,2,11,4,3,15,1,9,10,13,6,12
#
# 20
# 8
# 8,14,13,15,20,12,10,2,7,16,6,1,3,5,4,17,18,19,11,9