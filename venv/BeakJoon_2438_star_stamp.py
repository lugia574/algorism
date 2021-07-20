#별 찍기
star = int(input())
for i in range(1, star+1):
    print("*"*i)

for i in range(star-1, -1,-1):
    print(" "*i+"*"*(star-i))