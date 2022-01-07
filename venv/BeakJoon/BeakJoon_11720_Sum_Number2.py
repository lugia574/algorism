T = int(input())
num_list = list(input())
num_list = list(map(int,num_list))
def SumNums (T,num_list):
    sum = 0
    for i in range(T):
        sum += num_list[i]

    return sum

print(SumNums(T, num_list))

