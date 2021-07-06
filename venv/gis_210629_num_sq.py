num =  int(input())
def sol (num):
    sum = 0
    for i in range(1,num):
        sum+=i*(num+1)


    return sum

print(sol(num))