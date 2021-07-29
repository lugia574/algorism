# num = 156
# print(num%10)
# print((num//10)%10)
# print((num//100))
# print(num//100 - (num//10)%10 , (num//10)%10 - num%10)
#
#
# print(4177*0.85)
# #3550개
#
# print(4177-3550)
#
# ae = ''
# ae += str(5+1)
# print(ae)

# apt = [[0 for _ in range(15)] for _ in range(15)]
#
# for i in range(15):
#     apt[i][1] = 1
#     apt[0][i] = i
#
# for i in range(1, 15):
#     for j in range(2, 15):
#         apt[i][j] = apt[i][j - 1] + apt[i - 1][j];
#
#
#
#
# for x in apt:
#     print(x)
# import math
#
# print(round(4.58257569495584))
# print(int(math.sqrt(72)))
# print(8/2)

# test_list = []
#
# if test_list:
#     print(test_list)
# else:
#     print('wow')

arr = [[0 for col in range(3)]for row in range(3)]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == 0 or i == 2:
            arr[i][j] = 1
        elif i == 1 and (j == 0 or j == 2):
            arr[i][j] = 1
        else:
            arr[i][j] = 0


print(arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end=" ")

    print()