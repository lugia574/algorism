# 약수 구하기


num = int(input())


# 무지성 코딩
def measure (num):
    measurelist = []
    for i in range(1,num+1):
        if num % i == 0:
            measurelist.append(i)
    return measurelist

print(measure(num))

# 제곱근을 구해 그걸 이용한거
def measure2 (num):
    measurelist = []
    sqrt_num = int(num ** 0.5)
    
    for i in range(1, sqrt_num):
        if num % i == 0:
            measurelist.append(i)
            measure_num = int(num / i)
            measurelist.append(measure_num)

    if num/sqrt_num ==sqrt_num:
        measurelist.append(sqrt_num)


    measurelist.sort()
    return measurelist

print(measure2(num))



# 최대, 최솟값 구하기

numlist = list(map(int,input().split()))

# 그냥 무지성으로 한거
def min_max(list):
    min = 99999999
    max = 0
    for i in list:
        if min > i :
            min = i
        if max < i:
            max = i
    return min,max

# 배열 정열을 해 그리고 맨 첫값과 뒷값을 뽑는거야
def min_max2(list):
    tmp = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]<list[j]:
                tmp = list[i]
                list[i] = list[j]
                list[j] = tmp


    return list[0],list[-1]



print(min_max(numlist))
print(min_max2(numlist))

