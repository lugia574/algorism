A= int(input())
B= int(input())
C= int(input())

sum= str(A*B*C)
cnt = [0,0,0,0,0,0,0,0,0,0]
#print(type(sum))
list_num= list(sum)
list_num= list(map(int,list_num))

#print(list_num)
for i in range(10):
    for x in range(len(list_num)):
        if i == list_num[x]:
            cnt[i]+=1

for i in cnt:
    print(i)