# 한수
num = int(input())
def han (num):
    cnt = 0

    for i in range(1, num+1):
        if i <100:
            cnt +=1
        else:
            if (i//100 - (i//10)%10) == ((i//10)%10 - i%10):
                cnt += 1
    return cnt

print(han(num))


